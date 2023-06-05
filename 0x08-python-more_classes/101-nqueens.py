#!/usr/bin/python3

import sys


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        # Check if a queen can be placed at the given position without attacking any other queen

        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if there is a queen in the upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check if there is a queen in the upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_util(board, row):
        # Base case: If all queens are placed, print the solution
        if row == n:
            print(board)
            return

        # Recur for each column and try placing the queen in each position
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1  # Place the queen

                # Recur for the next row
                solve_util(board, row + 1)

                board[row][col] = 0  # Backtrack and remove the queen

    # Create an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N-Queens problem
    solve_util(board, 0)


# Main program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
