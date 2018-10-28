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

def utility(self, state, player):

def actions(self, state):

def result(self, state: Game.State, move_a):
    ##Illegal moves ha
    if move_a not in state.moves:
        return state
    state.player = to_move(state.player)
    state.board[move_a[1] - 1][move_a[2] - 1] = move_a[0]

def isCaptured(sefl, state: Game.State, posX, posY):
    stone = state.player
    stoneOpponent = to_move(stone)

    return isCapturedAux(state, posX, posY, )

def isCapturedAux(self, state: Game.State, posX, posY):


# recursive idea
# for every neighbours
#   if one of the them is blank -> return false
#   if one of them is the same color but we already have visited, ignore the stone
#   if all of them is of the opposite player -> return yes
#   if one of the neighbour is the same color, check that we did not visit the stone yet and
#       apply the same algorithm for this next stone

# -> problem if a stone has 2 opposite neighbours and 2 neighbours of
#    the same color but the first one is surrounded but opposite stones


def findNeighbours(sefl, state: Game.State, posX, posY):
    if posX == 1:
        if posY == 1:
            return [state.board[0][1], state.board[1][0]]
        elif posY == state.N:
            return [state.board[0][state.N - 2], state.board[1][state.N - 1]]
        else:
            return [state.board[0][posY - 2], state.board[1][posY - 1], state.board[0][posY]]
    elif posX == state.N:
        if posY == 1:
            return [state.board[state.N - 1][1], state.board[state.N - 2][0]]
        elif posY == state.N:
            return [state.board[state.N - 1][state.N - 2], state.board[state.N - 2][state.N - 1]]
        else:
            return [state.board[state.N - 1][posY - 2], state.board[state.N - 2][posY - 1], state.board[state.N - 1][posY]]
    elif posY == 1:
        return
    elif posY == state.N:
        return
    else:
        return [state.board[posX - 1][posY - 2], state.board[posX - 1][posY], state.board[posX - 2][posY - 1], state.board[posX][posY - 1]]
