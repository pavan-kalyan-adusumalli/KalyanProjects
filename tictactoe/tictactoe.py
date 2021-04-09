"""
Tic Tac Toe Player
"""

import math, copy, sys
sys.setrecursionlimit(300000)

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum([i.count('X') for i in board])
    o_count = sum([i.count('O') for i in board])
    if(terminal(board)):
        return X #if game over we can return anything
    elif(x_count == 0 and o_count == 0): #initial state of game
        return X
    elif(o_count < x_count):
        return O
    elif(x_count == o_count):
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if(terminal(board)): #if game over
        return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    else: #game is running
        actions = set([(i,j) for i in range(len(board)) for j in range(len(board[i])) if not board[i][j]])
        return actions


def result(board, action):
    # print('result func')
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_clone = copy.deepcopy(board)
    current_chance = player(board) #returns who's turn is now
    i, j = action[0], action[1]
    # print('board clone = ', board_clone)
    # print('current chance =', current_chance)
    # print('i,j',i,j)

    if(board_clone[i][j] == 'X' or board_clone[i][j]=='O'):
        raise Exception("You can't select occupied slot")

    elif(current_chance == 'X' and not board_clone[i][j]):
        # print(f'placing X on {i} {j}slot')
        board_clone[i][j] = 'X'

    elif(current_chance == 'O' and not board_clone[i][j]):
        board_clone[i][j] = 'O'
    # print("in func board_clone", board_clone)
    # print("in func orig board", board)
    return board_clone
    # raise NotImplementedError

def is_winner(board, cur_player): #helper function for winner
    for row in board:
        if(row.count(cur_player) == 3):
            # print(1)
            return True

    #vertical
    if(board[0][0]==cur_player and board[1][0]==cur_player and board[2][0]==cur_player):
        # print(2)
        return True
    if(board[0][1]==cur_player and board[1][1]==cur_player and board[2][1]==cur_player):
        # print(3)
        return True
    if(board[0][2]==cur_player and board[1][2]==cur_player and board[2][2]==cur_player):
        # print(4)
        return True
    
    if( (board[0][0]==cur_player and board[1][1]==cur_player and board[2][2]==cur_player) or (board[0][2]==cur_player and board[1][1]==cur_player and board[2][0]==cur_player)):
        # print(5)
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    is_x = is_winner(board, X)
    is_o = is_winner(board, O)
    if(is_x):
        return X
    elif(is_o):
        return O
    else:
        return None 


def terminal(board):
    # print('executing terminal func')
    # print(board)
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)): #if someone wins the game
        return True

    empty_spaces = 0
    for i in range(len(board)):#if there are any empty spaces
        for j in range(3):
            # print(board[i][j])
            if(not board[i][j]):
                empty_spaces += 1
    if(empty_spaces):#if there are 1 or more empty spaces
        return False
    else:
        return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board)):
        if(winner(board) is X):
            return 1
        elif(winner(board) is O):
            return -1
        else:
            return 0

def max_value(state):
    if(terminal(state)):
        return utility(state)
    v = float('-inf')
    # print("in max value()")
    # print("in max", state)
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    # #this line recursively checks opponent moves and picks the maximum value
    # print('v value', v)
    return v

def min_value(state):
    if(terminal(state)):
        return utility(state)
    v = float('inf')
    # print("in miin value(), state", state)
    # print(actions(state))
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    # this line recursively checks opponent(who's trying to increasing score(x-player))
    # and tries to reduce the score by picking the min score
    # print('v value', v)
    # print('final v', v)
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # print('you are inside minimax')
    # first get the current player
    if(player(board) == 'X'):
        # print('max the score')
        new_action = None
        initial_min_value = -2
        # print(initial_min_value,'initial max')
        for action in actions(board):
            cur_board = result(board, action)
            cur_min_value = min_value(cur_board)
            if(cur_min_value > initial_min_value):#choose the greatest from opponent's score(i.e. from min_value since X tries to increase score)
                initial_min_value = cur_min_value
                new_action = action
        # By the end of loop, action leads to max score will be retained
        # print('new action', new_action)
        return new_action
    else:
        # print("I'm O ill try to decrease the score")
        new_action = None
        initial_max_value = 2
        # print(actions(board))
        for action in actions(board):
            cur_board = result(board, action)
            cur_max_value = max_value(cur_board)
            # print('action, current max value', action , cur_max_value)
            if(cur_max_value < initial_max_value):#choose the least from opponent's score(i.e. from max_value since O tries to reduce score)
                initial_max_value = cur_max_value
                new_action = action
        # By the end of loop, action leads to min score will be retained
        # print('new action', new_action, initial_max_value)
        return new_action

