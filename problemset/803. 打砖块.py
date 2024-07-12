class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(i, j):
            # 从 [i, j] 开始新增了几个 2
            nonlocal row, col, grid
            if i < 0 or i == row or j < 0 or j == col or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        def w(x, y):
            # 填充回来，这一点确实中炮弹了
            # 并且上下左右连着天花板
            nonlocal grid, row, col
            return grid[x][y] == 1 and (
                x == 0 or 
                (x > 0 and grid[x - 1][y] == 2) or 
                (x < row - 1 and grid[x + 1][y] == 2) or
                (y > 0 and grid[x][y - 1] == 2) or
                (y < col - 1 and grid[x][y + 1] == 2)
            )
        
        # 时光倒流（数据处理的一种方式）
        row, col = len(grid), len(grid[0])
        ret = [0 for i in range(len(hits))]
        # 只有一行，怎么打都不会有砖块掉下去
        if row == 1:
            return ret
        # 炮弹打中的位置先减去 1
        for h in hits:
            grid[h[0]][h[1]] -= 1
        # 将连着天花板所有的 1 都变成 2
        for i in range(col):
            dfs(0, i)
        # 逆序处理所有的炮弹
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            grid[x][y] += 1
            if w(x, y):
                ret[i] = dfs(x, y) - 1
        return ret