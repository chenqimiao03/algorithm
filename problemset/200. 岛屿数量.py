# class DSU:

#     def __init__(self, n=1000001) -> None:
#         self._n = n
#         # 构建指向自己的指针
#         self._father = [i for i in range(n)]
#         # 每个集合的大小
#         self._size = [1 for i in range(n)]
#         self._stack = [0 for i in range(n)]
#         # 只有 grid[i][j] 是 1 的情况才算一个集合
#         self._sets = 0
    
#     def build(self, m):
#         self._sets = m

#     # i 号节点往上一直找，直到找到代表节点
#     def find(self, i):
#         size = 0
#         while i != self._father[i]:
#             self._stack[size] = i
#             size += 1
#             i = self._father[i]
#         # 扁平化
#         while size:
#             self._father[self._stack[size - 1]] = i
#             size -= 1
#         return i

#     def union(self, x, y):
#         fx = self.find(x)
#         fy = self.find(y)
#         if fx != fy:
#             # 小挂大
#             if self._size[fx] >= self._size[fy]:
#                 self._size[fx] += self._size[fy]
#                 self._father[fy] = fx
#             else:
#                 self._size[fy] += self._size[fx]
#                 self._father[fx] = fy
#             self._sets -= 1

#     def isSameSet(self, x, y):
#         return self.find(x) == self.find(y)

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # 二维数组平坦化（降维处理）
#         n, m = len(grid), len(grid[0])
#         dsu = DSU(n * m)
#         k = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '1':
#                     k += 1
#         dsu.build(k)
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '1':
#                     if j > 0 and grid[i][j - 1] == '1':
#                         dsu.union(i * m + j, i * m + j - 1)
#                     if i > 0 and grid[i - 1][j] == '1':
#                         dsu.union(i * m + j, (i - 1) * m + j)
#         return dsu._sets
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            nonlocal row, col
            # 边界
            if i < 0 or i == row or j < 0 or j == col or grid[i][j] != '1':
                return
            grid[i][j] = 0
            # 上
            dfs(grid, i - 1, j)
            # 下
            dfs(grid, i + 1, j)
            # 左
            dfs(grid, i, j - 1)
            # 右
            dfs(grid, i, j + 1)
        Islands = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    Islands += 1
                    dfs(grid, i, j)
        return Islands