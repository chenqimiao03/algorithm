class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.array = bytearray((size // 8) + 1)
        self.ones = 0
        self.zeros = self.size
        self.reverse = False

    def fix(self, idx: int) -> None:
        i, j = idx // 8, idx % 8
        if not self.reverse:
            # 位图所有位的状态，维持原始含义
            # 0：不存在
            # 1：存在
            if self.array[i] & (1 << j) == 0:
                self.zeros -= 1
                self.ones += 1
                self.array[i] |= 1 << j
        else:
            # 0：表示存在
            # 1：表示不存在
            if self.array[i] & (1 << j) != 0:
                self.zeros -= 1
                self.ones += 1
                # 两种等价写法
                # self.array[i] &= ~(1 << j)
                self.array[i] ^= (1 << j)

    def unfix(self, idx: int) -> None:
        i, j = idx // 8, idx % 8
        if not self.reverse:
            if self.array[i] & (1 << j) != 0:
                self.ones -= 1
                self.zeros += 1
                self.array[i] &= ~(1 << j)
        else:
            if self.array[i] & (1 << j) == 0:
                self.ones -= 1
                self.zeros += 1
                self.array[i] |= (1 << j)

    def flip(self) -> None:
        self.reverse = not self.reverse
        self.zeros, self.ones = self.ones, self.zeros

    def all(self) -> bool:
        return self.zeros == 0

    def one(self) -> bool:
        return self.ones != 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        ans = []
        for i in range(self.size // 8):
            for j in range(8):
                if not self.reverse:
                    ans.append('1' if (self.array[i] >> j) & 1 else '0')
                else:
                    ans.append('0' if (self.array[i] >> j) & 1 else '1')
        for j in range(self.size % 8):
            if not self.reverse:
                ans.append('1' if (self.array[self.size // 8] >> j) & 1 else '0')
            else:
                ans.append('0' if (self.array[self.size // 8] >> j) & 1 else '1')
        return ''.join(ans)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()