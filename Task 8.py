def print_board(board):
    """Print the chessboard."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at (row, col)."""
    
    # Check column above
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    """Backtracking recursive function to solve N-Queens."""
    if row == n:
        # All queens placed, store the solution
        solution = [r[:] for r in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print(f"Total Solutions for {n}-Queens: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_board(sol)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    n = 4  # You can change N
    n_queens(n)
