class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # n = len(nums)
        # cp = [0 for i in range(n)]
        # j, k = 0, 1
        # for i in range(n):
        #     if nums[i] % 2 == 0:
        #         cp[j] = nums[i]
        #         j += 2
        #     else:
        #         cp[k] = nums[i]
        #         k += 2
        # return cp
        n = len(nums)
        # 最后一个偶数应该摆放的位置
        e = 0
        # 最后一个奇数应该摆放的位置
        o = 1
        while e < n and o < n:
            # 永远只盯着最后一个数
            if nums[n - 1] % 2 == 0:
                nums[e], nums[n - 1] = nums[n - 1], nums[e]
                e += 2
            else:
                nums[o], nums[n - 1] = nums[n - 1], nums[o]
                o += 2
        return nums