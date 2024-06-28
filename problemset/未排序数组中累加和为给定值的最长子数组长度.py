class Solution:

    def maxlenEqualK(self, nums, target):
        HashMap = {0: -1} # 0 这个前缀和，在一个数字都没有的时候就存在了
        total = 0
        ret = 0
        for i in range(len(nums)):
            # 累加和
            total += nums[i]
            # 求 total - target 这个累加和最早出现的位置
            if HashMap.get(total - target, None) is not None:
                ret = max(ret, i - HashMap.get(total - target))
            if HashMap.get(total, None) is None:
                HashMap[total] = i
        return ret
