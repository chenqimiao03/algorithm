# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         # 共对角线：|当前的行 - 之前的行| = |当前的列 - 之前的列|
#         def check(path, i, j):
#             for k in range(i):
#                 # 当前列是否出现过
#                 if j == path[k] or \
#                     abs(i - k) == abs(path[k] - j): # 是否在对角线上
#                     return False
#             return True
#         def f(i, path, n):
#             if i == n:
#                 return 1
#             ret = 0
#             for j in range(n):
#                 if check(path, i, j):
#                     # path[row] = col
#                     path[i] = j
#                     ret += f(i + 1, path, n)
#             return ret
#         if n < 1:
#             return 0
#         return f(0, [None for i in range(n)], n)

# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         result = 0
#         column = set()
#         major = set()
#         sub = set()
#         def dfs(row):
#             nonlocal result
#             if row == n:
#                 result += 1
#                 return
#             for col in range(n):
#                 if col in column or row + col in major or row - col in sub:
#                     continue
#                 major.add(row + col) # 主对角线
#                 sub.add(row - col) # 次对角线
#                 column.add(col) # 列数
#                 dfs(row+1)
#                 major.remove(row + col)
#                 sub.remove(row - col)
#                 column.remove(col)
#         dfs(0)
#         return result

class Solution:
    def totalNQueens(self, n: int) -> int:
        # 用一个整型数据 col 的状态表示哪些列已经摆放了皇后，比如第一列已经摆放了皇后那么 col: 0x00000002
        def f(limit, col, major, sub):
            if col == limit:
                return 1
            ret = 0
            status = col | major | sub
            candidate = limit & (~status)
            # 尝试放皇后的位置
            place = 0
            while candidate != 0:
                place = candidate & (-candidate)
                candidate ^= place
                ret += f(limit, col | place, (major | place) << 1, (sub | place) >> 1)
            return ret
        if n < 1:
            return 0
        # 设置棋盘大小
        limit = ((1 << n) - 1)  & 0xffffffff
        return f(limit, 0, 0, 0)