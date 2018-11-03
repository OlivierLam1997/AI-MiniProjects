from copy import deepcopy

class Game:

## Steps:
##  1. Load_board: load a game board and show the state
##  2. To_move: Who is the next to move?
##  3. Terminal_test: Is the state terminal?
##  4. Utility:
##      if yes then returns 1 if player wins, -1 is loses, 0 in case of draw
##      if not then evaluates the state (the possibilities) of the player
##  5. Action: determinate possible actions to do at a state
##  6. Result: returns the successor state after playing the action


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

        assert n > 3, "rang of the board sould be at least 4 to play"  # ask teacher
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
            return 1
        if player == 2:
            print('Next player to move is the white')
            return 2

    #
    def terminal_test(self, state: State):
        stoneCaptured = None
        for i in range(state.N - 1):
            for j in range(state.N - 1):
                stoneCaptured = stoneCaptured or self.isCaptured(state, i + 1, j + 1)
        return (len(state.moves) == 0) or stoneCaptured


    def utility(self, state: State, player):
        if self.terminal_test(state):
            if self.isDraw(self, state):
                return 0
            elif state.player == player:
                return -1
            else:
                return 1
        else:
            self.eval_fn(self, state, player)

    #compute all the liberties of the groups of opponent stones: list called OppLiberties
    #compute all the liberties of our group of stones: list called UsLiberties

    def eval_fn(self, state: State, player):
        self.getGroupLiberties(self, state)
        if (min(UsLiberties) > min(OppLiberties)):
            return 1 / (min(OppLiberties))
        elif (min(UsLiberties) < min(OppLiberties)):
            return - 1 / (min(OppLiberties))
        else:
            if state.player == player:
                return 0.0001
            else:
                return -0.0001

    def getGroupLiberties(self, state: State):
        UsLiberties = []
        OppLiberties = []

    def getGroups(self, state: State, listOfGroups):
        stoneDiscovered = []
        stone = state.player

        for i in range(state.N):
            for j in range (state.N):
                

    def isDraw(self, state: State):
        player2 = self.to_move(state)
        state2 = deepcopy(state)
        state2.player = player2

        movesPlayer1 = self.actions(self, state)
        movesPlayer2 = self.actions(self, state2)

        return len(movesPlayer1.extend(movesPlayer2)) == 0

    def actions(self, state: State):
        state.moves = []
        for i in range(state.N):
            for j in range(state.N):
                stone = state.board[i][j]
                if stone == 0:
                    state2 = deepcopy(state)
                    state2.board[i][j] = state2.player
                    if not self.isCaptured(self, state2, i + 1, j + 1):
                        state.moves.append((state.player, i + 1, j + 1))
        return state.moves

    def result(self, state: State, move_a):
        ##Illegal moves ha
        if move_a not in state.moves:
            return state
        state.player = self.to_move(state.player)
        state.board[move_a[1] - 1][move_a[2] - 1] = move_a[0]
        return state

    # Method that defines if a stone would be captured at position (posX, posY)
    def isCaptured(self, state: State, posX, posY):
        neighbourIsCaptured = None

        # check if neighbours are captured first and make sure that the next neighbour
        # doesn't check the "capture" of this stone
        for n in self.findNeighbours(self, state, posX, posY):
            if (state.board[posY - 1][posX - 1] != state.board[n[1]][n[0]]):
                neighbourIsCaptured = neighbourIsCaptured or \
                                        self.isCapturedAux(self, state, n[0] + 1, n[1] + 1, posX, posY, [])

        # a stone is captured only if no neighbours is captured
        print(neighbourIsCaptured)
        return self.isCapturedAux(self, state, posX, posY, None, None, []) and (not neighbourIsCaptured)

    #
    def isCapturedAux(self, state: State, posX, posY, previousPosX, previousPosY, liberties):
        stone = state.board[posY - 1][posX - 1]
        for n in self.findNeighbours(self, state, posX, posY):
            print(n)
            stoneNeighbour = state.board[n[1]][n[0]]
            # print(stoneNeighbour)
            if (posX != previousPosX) & (posY != previousPosY) & (stoneNeighbour == stone):
                self.isCapturedAux(self, state, n[0] + 1, n[1] + 1, posX, posY, liberties)
        liberties.extend(self.getLiberties(self, state, posX, posY))
        print(liberties)
        return len(liberties) == 0

    # returns list of all liberties of one stone, with position X and Y (1 to N)
    def getLiberties(self, state: State, posX, posY):
        liberties = []

        for s in self.findNeighbours(self, state, posX, posY):
            stone = state.board[s[1]][s[0]]
            if stone == 0:
                liberties.append((stone, s[0], s[1]))

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
            return [(posX - 2, 1), (posX - 1, 2), (posX, 1)]
        elif posY == state.N:
            return [(posX - 2, state.N - 1), (posX - 1, state.N - 2), (posX, state.N - 1)]
        else:
            return [(posX - 1, posY - 2), (posX - 1, posY), (posX - 2, posY - 1), (posX, posY - 1)]





game = Game
state = game.load_board(game, "/Users/olivier/PycharmProjects/AI-MiniProjects/go.txt")
print(state.N)

print(state.board)

neighbours = game.findNeighbours(game, state, 3, 2)
lib = game.getLiberties(game, state, 3, 4)
cap = game.isCapturedAux(game, state, 3, 2)


print(neighbours)
print(lib)
print(cap)