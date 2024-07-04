class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # HashMap = {}
        # for num in nums:
        #     if HashMap.get(num, None) is None:
        #         HashMap[num] = 1
        # ret = 1
        # while True:
        #     if HashMap.get(ret) is None:
        #         return ret
        #     ret += 1
        # l 的左边，都是做到 i 位置放着 i + 1 的数的区域
        # [r...] 存放没用的数据
        # [1, r] 是可以收集全的，每个数字收集一个
        l, r = 0, len(nums)
        while l < r:
            if nums[l] == l + 1:
                l += 1
            # 检查 nums[l] - 1 位置上的数字和 l 位置上的数字是相同
            elif nums[l] <= l or nums[l] > r or nums[nums[l] - 1] == nums[l]:
                i, j = l, r - 1
                nums[i], nums[j] = nums[j], nums[i]
                r -= 1
            else:
                i, j = l, nums[l] - 1
                nums[i], nums[j] = nums[j], nums[i]
        return l + 1