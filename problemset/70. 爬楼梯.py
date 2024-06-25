class Solution:
    def climbStairs(self, n: int) -> int:
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        # if n < 3:
        #     return n
        # a, b = 1, 2
        # ret = None
        # for i in range(n - 2):
        #     ret = a + b
        #     a, b = b, ret
        # return ret
        """
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        cache = [None for i in range(n + 1)]
        def f(n):
            nonlocal cache
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                if cache[n] is not None:
                    return cache[n]
                # N 阶台阶的步数等于 n - 1 阶台阶数爬 1 步和 n - 2 阶台阶爬 2 步的和
                cache[n] = f(n - 1) + f(n - 2)
                return cache[n]
        return f(n)