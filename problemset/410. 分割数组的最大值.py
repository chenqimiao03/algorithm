class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """时间复杂度：O(N*log(N))
        空间复杂度：O(1)
        """
        # 画家问题
        def f(nums, limit):
            # 必须让数组 nums 中每一部分的累加和都小于等于 limit，需要划分成几个部分
            part = 1
            total = 0
            # 如 [5, 2, 3, 6, 5, 7, 2, 1], limit: 10
            # 5, 2, 3 一组
            # 6 单独一组
            # 5 单独一组
            # 7, 2, 1 一组
            for i in range(len(nums)):
                # 如果当前值都大于 limit，那么怎么划都划不出小于 limit 的子数组
                if nums[i] > limit:
                    return 2 ** 31 - 1
                if total + nums[i] > limit:
                    part += 1
                    total = nums[i]
                else:
                    total += nums[i]
            return part
        l = 0
        r = sum(nums)
        ret = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            if f(nums, m) <= k:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret