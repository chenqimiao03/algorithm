class Solution:
    def tribonacci(self, n: int) -> int:
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        ret = None
        for i in range(n - 2):
            ret = a[0] + a[1] + a[2]
            a[0], a[1], a[2] = a[1], a[2], ret
        return ret
