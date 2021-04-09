from tictactoe import *

board = [['O', 'X', 'X'], 
        ['O', None, None],
        [None, None, None]]
print(board)
# print(result(board, (1,1)))
print('original board', board)
print('winner', winner(board))
print('utility', utility(board))
print('player', player(board))
print('terminal', terminal(board))
print('available actions', actions(board))

# print(max_value(result(board, (2,0))))

m = -2
for action in actions(board):# for max player(X)
    # print(result(board, action))
    cur = min_value(result(board, action))
    print(cur)
    print(f"action {action}, final result of specific action = {cur}")
    if(cur > m):
        m = cur
        new_action = action
print("final action, final score", new_action, m)
# print(board)
