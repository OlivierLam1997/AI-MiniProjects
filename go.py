from copy import deepcopy

class Game:

    # Define new object, State
    class State:
        def __init__(self, player, N, moves, board):
            self.player = player
            self.N = N
            self.moves = moves
            self.board = board

    #
    def load_board(self, fileName):
        stream = open(fileName, 'r').read().replace('\n', '')
        n = int(stream[0])

        assert n >= 3 # to be sure that the board is big enough
        player = int(stream[2])
        board = [None] * n

        index = 3
        for i in range(n):
            board[i] = [None] * n
            for j in range(n):
                board[i][j] = int(stream[index])
                index += 1

        return Game.State(player, n, None, board)

    #
    def to_move(self, state: State):
        player = state.player
        if player == 1:
            print('Next player to move is the black')
            return 2
        if player == 2:
            print('Next player to move is the white')
            return 1

    #
    def terminal_test(self, state: State):
        stoneCaptured = None
        for i in range(state.N - 1):
            for j in range(state.N - 1):
                if state.board[j][i] != 0:
                    stoneCaptured = stoneCaptured or self.isCaptured(self, state, i + 1, j + 1)
                    print(stoneCaptured)

        return (len(state.moves) == 0) or stoneCaptured

    def utility(self, state: State, player):
        if self.terminal_test(self, state):
            if len(state.moves) == 0:
                return 0
            elif state.player == player:
                return -1
            else:
                return 1
        else:
            state2 = deepcopy(state)
            state2.player = self.to_move(self, state)

            minUsLiberties = min(self.getGroupLiberties(self, state))
            minOppLiberties = min(self.getGroupLiberties(self, state2))

            ratio = 1 / minOppLiberties

            if minUsLiberties > minOppLiberties:
                return ratio
            elif minUsLiberties < minOppLiberties:
                return -ratio
            else:
                if state.player == player:
                    return 0.0001
                else:
                    return -0.0001

    def getGroupLiberties(self, state: State):
        nbLibPerGroup = []
        for group in self.getGroups(self, state):
            groupLib = set()
            for s in group:
                groupLib.update(self.getLiberties(self, state, s[0] + 1, s[1] + 1))
            nbLibPerGroup.append(len(set(groupLib)))
        return nbLibPerGroup

    def getGroups(self, state: State):
        stoneDiscovered = set()
        listOfGroups = []

        for i in range(state.N):
            for j in range (state.N):

                if (j, i) not in stoneDiscovered and state.board[i][j] == state.player:
                    newGroup = self.getGroupsAux(self, state, j, i, set(), {(j, i)})
                    stoneDiscovered.update(newGroup)
                    listOfGroups.append(list(newGroup))
        return listOfGroups

    def getGroupsAux(self, state: State, coordX, coordY, traversed, group):
        for n in self.findNeighbours(self, state, coordX + 1, coordY + 1):
            if (n[0], n[1]) not in group and state.board[n[1]][n[0]] == state.player:
                stone = state.board[n[1]][n[0]]
                group.add((n[0], n[1]))
                traversed.add((coordX, coordY))

        return group.union(*[self.getGroupsAux(self, state, n0, n1, traversed, group)
            for (n0, n1) in
            filter(lambda nbr : state.board[nbr[1]][nbr[0]] == state.player and (nbr[0], nbr[1]) not in traversed,
                   self.findNeighbours(self, state, coordX + 1, coordY + 1))])

    def actions(self, state: State):
        state.moves = []
        for i in range(state.N):
            for j in range(state.N):
                stone = state.board[i][j]
                if stone == 0:
                    state2 = deepcopy(state)
                    state2.board[i][j] = state2.player
                    if not self.isCaptured(self, state2, j + 1, i + 1):
                        state.moves.append((state.player, i + 1, j + 1))
        return state.moves

    def result(self, state: State, move_a):
        ##Illegal moves ha
        if move_a not in state.moves:
            return state
        state.player = self.to_move(state.player)
        state.board[move_a[2] - 1][move_a[1] - 1] = move_a[0]
        return state

    def isCaptured(self, state: State, posX, posY):
        neighbourIsCaptured = None

        # check if neighbours are captured first and make sure that the next neighbour
        # doesn't check the "capture" of this stone
        for n in self.findNeighbours(self, state, posX, posY):
            if (state.board[posY - 1][posX - 1] != state.board[n[1]][n[0]]):
                neighbourIsCaptured = neighbourIsCaptured or \
                                        len(self.isCapturedAux(self, state, n[0] + 1, n[1] + 1, set(),
                                                           self.getLiberties(self, state, n[0] + 1, n[1] + 1))) == 0
        # a stone is captured only if no neighbours is captured
        return len(self.isCapturedAux(self, state, posX, posY, set(), self.getLiberties(self, state, posX, posY))) == 0 \
               and (not neighbourIsCaptured)

    def isCapturedAux(self, state: State, posX, posY, traversed, liberties):

        stone = state.board[posY - 1][posX - 1]
        for n in self.findNeighbours(self, state, posX, posY):
            stoneNeighbour = state.board[n[1]][n[0]]
            if (n[0] + 1, n[1] + 1) not in traversed and (stoneNeighbour == stone):
                liberties = liberties.union(self.getLiberties(self, state, n[0] + 1, n[1] + 1))
                traversed.add((posX, posY))

        return liberties.union(*[self.isCapturedAux(self, state, n0 +1, n1 +1, traversed, liberties)
                for (n0, n1) in
          filter(lambda nbr : state.board[nbr[1]][nbr[0]] == stone and (nbr[0] + 1, nbr[1] + 1) not in traversed,
                 self.findNeighbours(self, state, posX, posY))])

    # returns list of all liberties of one stone, with position X and Y (1 to N)
    def getLiberties(self, state: State, posX, posY):
        liberties = set()

        for s in self.findNeighbours(self, state, posX, posY):
            stone = state.board[s[1]][s[0]]
            if stone == 0:
                liberties.add((s[0], s[1]))

        return liberties

    # returns the coordinates(on the board -> 0 to N - 1)of all adjacent stones
    def findNeighbours(self, state: State, posX, posY):
        if posX == 1:
            if posY == 1:
                return[(0, 1), (1, 0)]
            elif posY == state.N:
                return [(0, state.N - 2), (1, state.N - 1)]
            else:
                return [(0, posY - 2),(1, posY - 1),(0, posY)]
        elif posX == state.N:
            if posY == 1:
                return [(state.N - 1, 1), (state.N - 2, 0)]
            elif posY == state.N:
                return [(state.N - 1, state.N - 2), (state.N - 2, state.N - 1)]
            else:
                return [(state.N - 1, posY - 2), (state.N - 2, posY - 1), (state.N - 1, posY)]
        elif posY == 1:
            return [(posX - 2, 0), (posX - 1, 1), (posX, 0)]
        elif posY == state.N:
            return [(posX - 2, state.N - 1), (posX - 1, state.N - 2), (posX, state.N - 1)]
        else:
            return [(posX - 1, posY - 2), (posX - 1, posY), (posX - 2, posY - 1), (posX, posY - 1)]


game = Game
state = game.load_board(game, "go.txt")
state.moves = game.actions(game, state)


print(game.utility(game, state, 1))
