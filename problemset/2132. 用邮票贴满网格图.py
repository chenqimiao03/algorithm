class Solution:

    def add(self, arr, a, b, c, d, k=1):
        arr[a][b] += k
        arr[c + 1][d + 1] += k
        arr[c + 1][b] -= k
        arr[a][d + 1] -= k

    def build(self, arr):
        # 用了一圈 0 包裹着真实数据
        for i in range(1, len(arr)):
            for j in range(1, len(arr[0])):
                arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    def sumRegion(self, arr, a, b, c, d):
        return arr[c][d] - arr[c][b - 1] - arr[a - 1][d] + arr[a - 1][b - 1]

    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        n, m = len(grid), len(grid[0])
        _sum = [[0 for i in range(m + 1)] for j in range(n + 1)]
        # 构建二维前缀和数组，快速区域累加和查询
        for i in range(n):
            for j in range(m):
                _sum[i + 1][j + 1] = grid[i][j]
        self.build(_sum)
        # 如果一个区域内都是 0 那么：
        # sumRegion(_sum, a, b, c, d) 必定为 0
        # 那么就可以在这个区域上贴上邮票
        diff = [[0 for i in range(m + 2)] for j in range(n + 2)]
        a = 1
        c = a + h - 1
        while c <= n:
            b = 1
            d = b + w - 1
            while d <= m:
                if self.sumRegion(_sum, a, b, c, d) == 0:
                    self.add(diff, a, b, c, d, 1)
                b += 1
                d += 1
            a += 1
            c += 1
        self.build(diff)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and diff[i + 1][j + 1] == 0:
                    return False
        return True
