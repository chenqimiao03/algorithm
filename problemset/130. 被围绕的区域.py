class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            nonlocal rows, cols
            if i < 0 or i == rows or j < 0 or j == cols or board[i][j] != 'O':
                return 
            board[i][j] = 'F'
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)
        rows, cols = len(board), len(board[0])
        # 从边界开始
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(board, 0, col)
            if board[rows - 1][col] == 'O':
                dfs(board, rows - 1, col)
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(board, row, 0)
            if board[row][cols - 1] == 'O':
                dfs(board, row, cols - 1)
        for row in range(rows):
            for col in range(cols):
                # 被 X 包围的 O 全部变为 X
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                # 边界上的 O
                if board[row][col] == 'F':
                    board[row][col] = 'O'
        return