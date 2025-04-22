def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col]:
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)]:
                return False
            if col + (row - i) < n and board[i][col + (row - i)]:
                return False
        return True

    def solve(row):
        if row == n:
            result = []
            for i in range(n):
                for j in range(n):
                    if board[i][j]:
                        result.append(j + 1)  # 1-based index
            solutions.append(result)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions[0] if solutions else []