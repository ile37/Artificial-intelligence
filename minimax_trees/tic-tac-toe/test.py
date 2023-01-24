import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None


board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board = [[X, X, EMPTY],
        [O, EMPTY, X],
        [EMPTY, O, O]]


print(board)
print()
print(ttt.minimax(board))
