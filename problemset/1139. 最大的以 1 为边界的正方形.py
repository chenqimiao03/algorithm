class Solution:

    def get(self, g, i, j):
        return 0 if i < 0 or j < 0 else g[i][j]

    def build(self, n, m, g):
        for i in range(n):
            for j in range(m):
                g[i][j] += self.get(g, i, j - 1) + self.get(g, i - 1, j) - self.get(g, i - 1, j - 1)
    
    def sum(self, g, a, b, c, d):
        return 0 if a > c else g[c][d] - self.get(g, c, b-1) - self.get(g, a - 1, d) + self.get(g, a - 1, b - 1)

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        self.build(n, m, grid)
        if self.sum(grid, 0, 0, n - 1, m - 1) == 0:
            return 0
        ret = 1
        for a in range(n):
            for b in range(m):
                # 剪枝
                c = a + ret
                d = b + ret
                k = ret + 1
                while c < n and d < m:
                    # 大正方形面积 - 小正方形面积 是否等于周长
                    if self.sum(grid, a, b, c, d) - self.sum(grid, a + 1, b + 1, c - 1, d - 1) == ((k - 1) << 2):
                        ret = k
                    c += 1
                    d += 1
                    k += 1
        return ret * ret

