#!/usr/bin/python3

"""101-nqueens finds all possible solutions the N queens puzzle, including
translations and reflections.

Attempted virtual backtracking without recursion. In local tests process will
start to slow down visibly for N > 8, and is successful up to N = 11 but
will be killed if used for N > 11. Recursion could allow for a lighter weight
process, but it's not yet apparent to this student how to retain a record of
which solutions are already derived with that method.

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candidates (list) of (list) of (list) of (int): list of all successful
        solutions for given amount of columns checked

"""
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board, N):
    for i in range(N):
        print("{}".format("." * board[i] + "Q" + "." * (N - board[i] - 1)))

def solve_nqueens(N):
    board = [-1] * N
    solve_nqueens_util(board, 0, N)

def solve_nqueens_util(board, row, N):
    if row == N:
        print_solution(board, N)
        print()
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens_util(board, row + 1, N)
            board[row] = -1

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()
