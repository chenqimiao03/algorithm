class Solution:
    """
    验证链接：https://leetcode.cn/problems/missing-number/
    """
    def missingNumber(self, nums: List[int]) -> int:
        eor = 0
        for i in range(len(nums) + 1):
            eor ^= i
        for num in nums:
            eor ^= num
        return eor
