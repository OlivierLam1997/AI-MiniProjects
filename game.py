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
def load_board(self, stream):
    str = open(stream, 'r').read().replace('\n', '')
    n = int(str[0])
    player = int(str[2])
    board = list()

    index = n
    for i in range(n):
        board[i] = list()
        for j in range(n):
            board[i][j] = int(str(index))
            index += 1
            
    return Game.State(player, n, None, board)


## to_move done for the state representation. Don't touch without consultation
def to_move(self, state):
    player = state[0]
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

def result(self, state, move_a):
    ##check if the move is valid -> check if move_a is in the list of all valid moves

    state[0] = to_move(self, state)
    state[]
