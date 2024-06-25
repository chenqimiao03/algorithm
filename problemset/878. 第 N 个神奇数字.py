class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a, b):
            """求 a 和 b 的最大公约数
            """
            return a if b == 0 else gcd(b, a % b)
        def lcm(a, b):
            """求 a 和 b 的最小公倍数
            """
            return a // gcd(a, b) * b
        _lcm = lcm(a, b)
        ret = 0
        l, r, m = 0, n * min(a, b), 0
        while l <= r:
            m = (l + r) // 2
            if m // a + m // b - m // _lcm >= n:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret % 1000000007