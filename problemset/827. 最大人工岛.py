class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, landId):
            nonlocal row, col
            if i < 0 or i == row or j < 0 or j == col or grid[i][j] != 1:
                return 
            grid[i][j] = landId
            dfs(grid, i - 1, j, landId)
            dfs(grid, i + 1, j, landId)
            dfs(grid, i, j - 1, landId)
            dfs(grid, i, j + 1, landId)
        row, col = len(grid), len(grid[0])
        landId = 2
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(grid, i, j, landId)
                    landId += 1
        cnts = [0 for i in range(landId)]
        ret = 0
        # 统计每块岛的面积
        for i in range(row):
            for j in range(col):
                if grid[i][j] > 1:
                    cnts[grid[i][j]] += 1
                    ret = max(ret, cnts[grid[i][j]])
        visited = [False for i in range(landId)]
        for i in range(row):
            for j in range(col):
                # 最多允许一格 0 变 1
                if grid[i][j] == 0:
                    top = grid[i - 1][j] if i > 0 else 0
                    bottom = grid[i + 1][j] if i + 1 < row else 0
                    left = grid[i][j - 1] if j > 0 else 0
                    right = grid[i][j + 1] if j + 1 < col else 0
                    visited[top] = True
                    a = 1 + cnts[top]
                    # 去重
                    if not visited[bottom]:
                        visited[bottom] = True
                        a += cnts[bottom]
                    if not visited[left]:
                        visited[left] = True
                        a += cnts[left]
                    if not visited[right]:
                        visited[right] = True
                        a += cnts[right]
                    visited[top] = False
                    visited[bottom] = False
                    visited[left] = False
                    visited[right] = False
                    ret = max(ret, a)
        return ret
