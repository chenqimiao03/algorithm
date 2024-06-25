class MyCircularQueue:
    """
    验证链接：https://leetcode.cn/problems/design-circular-queue/
    """

    def __init__(self, n):
        self.cap = n
        self._vals = [None for _ in range(self.cap)]
        self.first, self.last, self._size = 0, 0, 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self._vals[self.last] = value
        self.last = 0 if self.last == self.cap - 1 else self.last + 1
        self._size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.first = 0 if self.first == self.cap - 1 else self.first + 1
        self._size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self._vals[self.first]

    def Rear(self):
        if self.isEmpty():
            return -1
        last = self.cap - 1 if self.last == 0 else self.last - 1
        return self._vals[last]

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self.cap
