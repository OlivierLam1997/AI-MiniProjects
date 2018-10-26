class game:

## Steps:
##  1. Load_board: load a game board and show the state
##  2. To_move: Who is the next to move?
##  3. Terminal_test: Is the state terminal?
##  4. Utility:
##      if yes then returns 1 if player wins, -1 is loses, 0 in case of draw
##      if not then evaluates the state (the possibilities) of the player
##  5. Action: determinate possible actions to do at a state
##  6. Result: returns the successor state after playing the action


## load_board done for the state representation. Don't touch without consultation
def load_board(self, stream):
    str = open(stream, 'r').read().replace('\n', '')
    row_str = str[0]
    column_str = str[0]
    state = []
    state.append(int(str[2]))
    row = int(row_str)
    column = int(column_str)
    index = 4
    for i in range(row):
        for j in range(column):
            state.append(int(str[index]))
            index += 1
    return state


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
