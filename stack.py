class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack:

    def __init__(self, n):
        self._vals = [None for _ in range(n)]
        self.cap = n
        self._size = 0

    def push(self, val):
        if self._size == self.cap:
            raise Full('the stack is full')
        self._vals[self._size] = val
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty('the stack is empty')
        r = self._vals[self._size - 1]
        self._size -= 1
        return r

    def top(self):
        if self._size == 0:
            raise Empty('the stack is empty')
        return self._vals[self._size - 1]

    def size(self):
        return self._size

    def __str__(self):
        return str(self._vals)


class MyStack:
    """
    使用队列实现栈
    题目出处：https://leetcode.cn/problems/implement-stack-using-queues/description/
    """

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if self.empty():
            raise Empty('the stack is empty')
        if len(self.q1):
            for i in range(len(self.q1)):
                self.q2.append(self.q1[i])
            self.q1.clear()
        return self.q2.pop()

    def top(self):
        if self.empty():
            raise Empty('the stack is empty')
        if len(self.q1):
            for i in range(len(self.q1)):
                self.q2.append(self.q1[i])
            self.q1.clear()
        return self.q2[-1]

    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0


class MinStack:
    """
    最小栈
    题目出处：https://leetcode.cn/problems/min-stack/description/
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val):
        self.s1.append(val)
        self.s2.append(val if len(self.s2) == 0 else min(val, self.s2[-1]))

    def pop(self):
        self.s1.pop()
        self.s2.pop()

    def top(self):
        return self.s1[-1]

    def getMin(self):
        return self.s2[-1]


if __name__ == '__main__':
    s = ArrayStack(10)
    for i in range(10):
        s.push(i)
    print(s)
    print(s.top())
    print(s.size())
    for i in range(9, -1, -1):
        assert s.top() == i
        assert s.pop() == i
    print(s.size())
    s.push(100)
    print(s.size())
    print(s)
