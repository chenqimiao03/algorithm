class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _pow(n, x):
            if n == 0:
                return 1.
            # x^n = x^{n//2} * x^{n//2}
            half = _pow(n // 2, x)
            if n & 1:
                return x * half * half
            return half * half
        if n < 0:
            return 1. / _pow(-n, x)
        return _pow(n, x)
