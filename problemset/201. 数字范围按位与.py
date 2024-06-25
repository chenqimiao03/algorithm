class Solution:
    """
    验证链接：https://leetcode.cn/problems/bitwise-and-of-numbers-range/
    """
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            # right 每次减去它最右侧的 1，如果 right - 1 还在 [left, right] 这个区间中，那么最右侧的 1 一定不能保留下来
            right -= right & (-right)
        return right
