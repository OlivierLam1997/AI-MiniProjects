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


## Define new object, State
    class State:
        def __init__(self, player, N, moves, board):
            self.player = player
            self.N = N
            self.moves = moves
            self.board = board



## load_board done for the state representation. Don't touch without consultation
def load_board(self, fileName):
    stream = open(fileName, 'r').read().replace('\n', '')
    n = int(stream[0])

    assert n > 3, "rang of the board sould be at least 4 to play" ##ask teacher
    player = int(stream[2])
    board = list()

    index = n
    for i in range(n):
        board[i] = list()
        for j in range(n):
            board[i][j] = int(stream(index))
            index += 1

    return Game.State(player, n, None, board)


## to_move done for the state representation. Don't touch without consultation
def to_move(self, state : Game.State):
    player = state.player
    if player == 1:
        print('Next player to move is the black')
        return 1
    if player == 2:
        print('Next player to move is the white')
        return 2


##To do:
def terminal_test(self, state):
    return len(state.moves) == 0

def utility(self, state, player):

def actions(self, state : Game.State):
    state.moves=[]
    for i in range(state.N):
        for j in range(state.N):
            stone = state.board[i - 1][j - 1]
            if stone==0 and isCaptured(state,i,j)==False:
                state.moves.append((state.player,i,j))
    return state.moves



def result(self, state: Game.State, move_a):
    ##Illegal moves ha
    if move_a not in state.moves:
        return state
    state.player = to_move(state.player)
    state.board[move_a[1] - 1][move_a[2] - 1] = move_a[0]
    return None

##
def isCaptured(sefl, state: Game.State, posX, posY):
    neighbourIsCaptured = None

    ## check if neighbours are captured first and make sure that the next neighbour doesn't check the "capture" of this stone
    for n in findNeighbours(state, posX, posY):
        neighbourIsCaptured = neighbourIsCaptured or isCapturedAux(state, n[0] + 1, n[1] + 1, posX, posY, None)

    #a stone is captured only if no neighbours is captured
    return isCapturedAux(state, posX, posY, None, None, None) and (not neighbourIsCaptured)


##
def isCapturedAux(self, state: Game.State, posX, posY, previousPosX, previousPosY, liberties):
    stone = state.board[posX - 1][posY - 1]
    for n in findNeighbours(state, posX, posY):
        stoneNeighbour = state.board[n[0]][n[1]]
        if (posX != previousPosX) & (posY != previousPosY) & (stoneNeighbour == stone):
            isCapturedAux(state, n[0], n[1], posX, posY, liberties)
    liberties.extend(getLiberties(state, posX, posY))
    return len(liberties) == 0


## returns list of all liberties of one stone, with position X and Y (1 to N)
def getLiberties(self, state: Game.State, posX, posY):
    liberties = list()

    for s in findNeighbours(state, posX, posY):
        stone = state.board[s[0]][s[1]]
        if stone == 0:
            liberties.append(stone)

    return liberties

## returns the coordinates(on the board -> 0 to N - 1)of all adjacent stones
def findNeighbours(sefl, state: Game.State, posX, posY):
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
