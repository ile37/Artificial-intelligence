"""
Tic Tac Toe Player
"""

import copy

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
    x_count = 0
    o_count = 0

    for row in board:
        for mark in row:
            if mark == X:
                x_count += 1
            if mark == O:
                o_count += 1

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, mark in enumerate(row):
            if mark == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    i, j = action

    if 0 <= i <= 2 and 0 <= j <= 2 and board_copy[i][j] == EMPTY:
        board_copy[i][j] = player(board_copy)
    else:
        raise Exception

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #TODO optimize winner function
    # rows
    for i, row in enumerate(board):
        current_mark = row[0]
        for j in range(0, 3):
            if current_mark == None:
                break
            if current_mark != row[j]:
                break
            if j == 2:
                return current_mark
    # columns
    for j in range(0, 3):
        current_mark = board[0][j]
        for i in range(1,3):
            if current_mark == None:
                break
            if current_mark != board[i][j]:
                break
            if i == 2:
                return current_mark

    # diagonal
    current_mark = board[0][0]
    for i in range(1,3):
        if current_mark == None:
            break
        if current_mark != board[i][i]:
            break
        if i == 2:
            return current_mark

    current_mark = board[0][2]
    offset = 0
    for i in range(1,3):
        if current_mark == None:
            break
        if current_mark != board[i][i-offset]:
            break
        if i == 2:
            return current_mark
        offset += 2

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for row in board:
            for mark in row:
                if mark == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_mark = winner(board)
    if winner_mark == X:
        return 1
    elif winner_mark == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        v, action = minimax_recursion(board)
        return action


def minimax_recursion(board):
    """
    Starts the minimax search and returns value of position and the best move moving forward
    """
    if terminal(board):
        return utility(board), (-1,-1)
    else:
        if player(board) == X:
            return max_value(board)
        else:
            return min_value(board)


def max_value(board):
    values = []
    recorded_actions = []
    for action in actions(board):
        v, _ = minimax_recursion(result(board, action))
        values.append(v)
        recorded_actions.append(action)
    max_value = max(values)
    return max_value, recorded_actions[values.index(max_value)]


def min_value(board):
    values = []
    recorded_actions = []
    for action in actions(board):
        v, _ = minimax_recursion(result(board, action))
        values.append(v)
        recorded_actions.append(action)
    min_value = min(values)
    return min_value, recorded_actions[values.index(min_value)]
