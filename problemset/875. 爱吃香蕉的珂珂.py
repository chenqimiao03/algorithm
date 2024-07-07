class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(piles, s):
            # 向上取整功能
            ret = 0
            for pile in piles:
                # (a / b) 向上取整，如果 a 和 b 都是非负数，可以写成 (a + b - 1) / b
                ret += (pile + s - 1) // s
            return ret

        # 最小且达标的速度，[l, r]
        l = 1
        r = max(piles)
        ret = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            # 查看当前速度能否在 h 的时间内吃完所有香蕉
            if f(piles, m) <= h:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret