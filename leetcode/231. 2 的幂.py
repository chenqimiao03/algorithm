class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # 一个数如果是 2 的幂，那么它的二进制 1 的个数必定是 1
        return n == (n & (-n))
