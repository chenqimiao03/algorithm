class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # dq = [[0, 0] for i in range(100001)]
        # h, t = 0, 0
        # ret = -2 ** 31
        # n = len(points)
        # # abs(x_i - x_j) <= k
        # # y - x 的值最大
        # for r in range(n):
        #     x, y = points[r]
        #     # x - dq[0][0] > k
        #     # 头部元素与当前元素的距离超过 k
        #     while h < t and dq[h][0] + k < x:
        #         h += 1
        #     if h < t:
        #         ret = max(ret, y + dq[h][1] + x - dq[h][0])
        #     while h < t and dq[t - 1][1] - dq[t - 1][0] <= y - x:
        #         t -= 1
        #     dq[t][0] = x
        #     dq[t][1] = y
        #     t += 1
        # return ret
        from collections import deque
        dq = deque()
        ret = -2 ** 31
        n = len(points)
        for r in range(n):
            x, y = points[r][0], points[r][1]
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                ret = max(ret, dq[0][1] + x + y - dq[0][0])
            while dq and (dq[-1][2] <= y - x):
                dq.pop()
            dq.append([x, y, y - x])
        return ret
