class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def f(batteries, m, n):
            """判断当前电量能不能是 n 台电脑同时运行 m 分钟
            """
            ret = 0
            for battery in batteries:
                # 不是碎片电池
                if battery > m:
                    n -= 1
                # 碎片电池
                else:
                    ret += battery
                if ret >= n * m:
                    # 碎片电量大于等于台数乘上同时运行的分钟数
                    return True
            return False

        l = 0
        r = sum(batteries)
        ret = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            if f(batteries, m, n):
                ret = m
                l = m + 1
            else:
                r = m - 1
        return ret