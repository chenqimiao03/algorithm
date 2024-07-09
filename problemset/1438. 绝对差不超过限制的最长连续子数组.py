class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 滑动窗口+单调队列
        def ok(dq1, dq2, limit, number):
            MAX = max(nums[dq1[0]], number) if dq1 else number
            MIN = min(nums[dq2[0]], number) if dq2 else number
            return (MAX - MIN) <= limit
        
        from collections import deque
        dq1 = deque() # 维持窗口的最大值，大->小
        dq2 = deque() # 维持窗口的最小值，小->大
        n =len(nums)
        ret = 0
        r = 0
        # 如果一个窗口 [l,...,r) 达标了，那么再怎么缩减窗口都是达标的
        for l in range(n):
            # 下一个即将进入窗口的数的位置
            # 有下一个数并且下一个数符合最大值减最小值不超过 limit，将 nums[r] 放到窗口中
            while r < n and ok(dq1, dq2, limit, nums[r]):
                while dq1 and nums[dq1[-1]] <= nums[r]:
                    dq1.pop()
                dq1.append(r)
                while dq2 and nums[dq2[-1]] >= nums[r]:
                    dq2.pop()
                dq2.append(r)
                r += 1
            ret = max(ret, r - l)
            # 将 nums[l] 从窗口中弹出
            if dq1 and dq1[0] == l:
                dq1.popleft()
            if dq2 and dq2[0] == l:
                dq2.popleft()
        return ret