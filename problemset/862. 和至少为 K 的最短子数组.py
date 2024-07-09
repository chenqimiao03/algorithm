class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 滑动窗口+前缀和
        from collections import deque
        dq = deque()
        n = len(nums)
        cusum = [0]
        ret = 2 ** 31 - 1
        for i in range(n):
            cusum.append(cusum[-1] + nums[i])
        for r in range(n + 1):
            # 当前的前缀和减去前一部分的前缀和（缩减窗口）看是否能达标
            # 达标就计算答案
            while dq and (cusum[r] - cusum[dq[0]]) >= k:
                ret = min(ret, r - dq.popleft())
            # 维持 小->大 的单调队列
            # 后续的前缀和如果减去当前的 cusum[r] 都不达标，那么减去比 cusum[r] 大的更加不可能达标（最短的）
            while dq and cusum[dq[-1]] >= cusum[r]:
                dq.pop()
            dq.append(r)
        return ret if ret != 2 ** 31 - 1 else -1