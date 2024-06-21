class Solution:
    """
    1162261467 是 int 范围内，最大的 3 的幂，它是 3 的 19 次方
    """
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
