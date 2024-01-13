#!/usr/bin/python3
""" This module solves the challenge of N non-attacking queens on an
NxN chessboard
"""

import sys


def is_safe(board, row, col, N):
    """ Check if there is a queen in the same row"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board, col, N, solutions):
    """ function to place Queens on board"""
    if col == N:
        solutions.append(list(enumerate(board)))
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = row
            solve_nqueens_util(board, col + 1, N, solutions)
            board[col] = -1


def solve_nqueens(N):
    """ Checks if N is a number"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
