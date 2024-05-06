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
