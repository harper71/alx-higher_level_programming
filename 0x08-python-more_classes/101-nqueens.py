#!/usr/bin/python3
import sys
""" an N queen game"""


def is_safe(board, row, col, n):
    """Check if placing a queen at the specified position is safe."""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N queens problem.

    Args:
        n (int): the rows
    """
    def backtrack(row, board):
        if row == n:
            return [board[:]]

        solutions = []
        for col in range(n):
            """Recursive backtracking function to find solutions."""
            if is_safe(board, row, col, n):
                board[row] = col
                solutions.extend(backtrack(row + 1, board))
        return solutions

    solutions = backtrack(0, [-1] * n)
    return [[(i, col) for i, col in enumerate(solution)]
            for solution in solutions]


def print_solution(solution):
    """prints the solution

    Args:
        solution (int): all rows printed
    """
    for row, col in solution:
        print("[{}, {}]".format(row, col), end=" ")
    print()


if __name__ == "__main__":
    """runs the game
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print_solution(solution)
