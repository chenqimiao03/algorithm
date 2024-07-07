class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def f(nums, limit):
            # nums 中任意两数的差值都小于等于 limit
            # 这样的数字配对有几对
            ret = 0
            r = 0
            # 滑动窗口
            for l in range(len(nums)):
                while r + 1 < len(nums) and nums[r + 1] <= nums[l] + limit:
                    r += 1
                ret += r - l
            return ret
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        ret = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            # 以 m 为差值的数字对大于等于 k，包含 k
            if f(nums, m) >= k:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret