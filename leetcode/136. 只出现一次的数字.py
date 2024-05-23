class Solution:
    """
    验证链接：https://leetcode.cn/problems/single-number/
    """
    def singleNumber(self, nums: List[int]) -> int:
        eor = 0
        for num in nums:
            eor ^= num
        return eor
