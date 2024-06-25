class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        j = 0 # 数组非零数字的尾指针
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
