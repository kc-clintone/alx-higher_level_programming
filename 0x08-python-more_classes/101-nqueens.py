#!/usr/bin/python3
"""The n-queen puzzle, evee had of that?"""

import sys

def init_board(n):
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)
def board_deepcopy(board):
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)
def get_solution(board):
    sol = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == "Q":
                sol.append([row, column])
                break
    return (sol)
def xout(board, row, col):
    for column in range(col + 1, len(board)):
        board[row][column] = "x"
    for column in range(col - 1, -1, -1):
        board[row][column] = "x"
    for row in range(row + 1, len(board)):
        board[r][col] = "x"
    for row in range(row - 1, -1, -1):
        board[row][col] = "x"
    column = col + 1
    for row in range(row + 1, len(board)):
        if column >= len(board):
            break
        board[row][column] = "x"
        column += 1
    column = col - 1
    for row in range(row - 1, -1, -1):
        if column < 0:
            break
        board[row][column]
        column -= 1
    column = col + 1
    for row in range(row - 1, -1, -1):
        if column >= len(board):
            break
        board[row][column] = "x"
        column += 1
    column = col - 1
    for row in range(row + 1, len(board)):
        if column < 0:
            break
        board[row][column] = "x"
        column -= 1
def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)
    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
