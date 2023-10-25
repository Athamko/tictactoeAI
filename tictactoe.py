"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    # counts how many Xs or Ys there are
    for row in board:
        for square in row:
            if square == None:
                continue
            elif square == X:
                x_count += 1
            elif square == O:
                o_count += 1

    # returns whose turn it is
    if x_count == 0:
        return X
    elif x_count > o_count:
        return O
    elif x_count == o_count:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    row_num = 0
    cell_num = 0
    action_set = set()

    for row in board:
        for cell in row:
            if cell == None:
                action_set.add((row_num, cell_num))
                cell_num += 1
            else:
                cell_num += 1
        cell_num = 0
        row_num += 1

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temporary_board = [row[:] for row in board]

    temporary_board[action[0]][action[1]] = player(board)

    return temporary_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    X_or_O = 0

    while X_or_O < 2:
        if X_or_O == 0:
            checking_player = X
        elif X_or_O == 1:
            checking_player = O
        else:
            return None

        variable = 0

        # cheking for horizontal win

        while variable < 3:
            print(variable)
            print(board)
            if (
                checking_player == board[variable][0]
                and checking_player == board[variable][1]
                and checking_player == board[variable][2]
            ):
                return checking_player
            variable += 1
        variable = 0

        # checking for vertical win
        while variable < 3:
            if (
                checking_player == board[0][variable]
                and checking_player == board[1][variable]
                and checking_player == board[2][variable]
            ):
                return checking_player
            variable += 1
        variable = 0

        # checking for diagonal win
        if (
            checking_player == board[0][0]
            and checking_player == board[1][1]
            and checking_player == board[2][2]
        ):
            return checking_player
        elif (
            checking_player == board[0][2]
            and checking_player == board[1][1]
            and checking_player == board[2][0]
        ):
            return checking_player

        if X_or_O < 1:
            X_or_O += 1
            continue
        else:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for row in board:
            for cell in row:
                if cell == None:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = -float("inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                break  # beta cut-off
        return v

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                break  # alpha cut-off
        return v

    if terminal(board):
        return None

    best_move = None
    if player(board) == X:
        best_value = -float("inf")
        for action in actions(board):
            value = min_value(result(board, action), -float("inf"), float("inf"))
            if value > best_value:
                best_value = value
                best_move = action
    elif player(board) == O:
        best_value = float("inf")
        for action in actions(board):
            value = max_value(result(board, action), -float("inf"), float("inf"))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move


"""""
print(
    "This is the next move:",
    minimax([[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]),
)
"""
