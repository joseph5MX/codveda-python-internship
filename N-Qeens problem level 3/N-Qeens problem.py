def is_safe(board, row, col, n):
    # Check this column on rows above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n, solutions):
    if row == n:
        # Found a valid arrangement — save a copy of it
        solution = ["".join("Q" if cell else "." for cell in r) for r in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0  # backtrack

def print_solution(solution):
    for row in solution:
        print(row)
    print()

def main():
    n = int(input("Enter the size of the board (N): "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve(board, 0, n, solutions)

    if not solutions:
        print(f"No solutions exist for N = {n}.")
        return

    print(f"Found {len(solutions)} solution(s) for N = {n}.\n")
    show_all = input("Show all solutions? (y/n): ").strip().lower()

    if show_all == "y":
        for idx, sol in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            print_solution(sol)
    else:
        print("First solution:")
        print_solution(solutions[0])

if __name__ == "__main__":
    main()