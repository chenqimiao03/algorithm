class Solution:

    def __init__(self):
        self.min_value = -2 ** 31
        self.max_value = 2 ** 31 - 1

    def add(self, a, b):
        def _add(a, b):
            ans = 0
            while b != 0:
                ans = (a ^ b) & 0xffffffff
                # 保存进位信息
                b = ((a & b) << 1) & 0xffffffff
                a = ans
            return ans

        ans = _add(a, b)
        return -_add(((~ans) & 0x7FFFFFFF), 1) if ans & 0x80000000 else ans

    def neg(self, n):
        if n > 0:
            return ~self.add(n, -1)
        elif n == 0:
            return 0
        else:
            return self.add((~n & 0x7fffffff), 1)

    def minus(self, a, b):
        # a - b = a + (-b) = a + (~b + 1)
        return self.add(a, self.neg(b) & 0xffffffff)

    def _divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("b cannot equal 0")
        x = self.neg(a) if a < 0 else a
        y = self.neg(b) if b < 0 else b
        ans = 0
        for idx in range(30, -1, -1):
            if (x >> idx) >= y:
                ans |= 1 << idx
                x = self.minus(x, y << idx)
        return ans if (a & 0x80000000) == (b & 0x80000000) else ~self.minus(ans, 1)

    def divide(self, a: int, b: int) -> int:
        if a == self.min_value and b == self.min_value:
            return 1
        if a != self.min_value and b != self.min_value:
            return self._divide(a, b)
        if b == self.min_value:
            return 0
        # a 是整数最小并且 b 是 -1
        # 返回整数最大
        if a == self.min_value and b == -1:
            return self.max_value
        a = self.add(a, b if b > 0 else self.neg(b))
        ans = self._divide(a, b)
        offset = self.neg(1) if b > 0 else 1
        return self.add(ans, offset)