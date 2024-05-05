class ListNode:

    def __init__(self, val, nxt=None):
        self.next = nxt
        self.val = val


class Empty(Exception):
    pass


class Full(Exception):
    pass


class LinkedQueue:

    def __init__(self):
        self.first = ListNode(None)
        self.last = self.first
        self.cnt = 0

    def isEmpty(self):
        """
        判断队列是不是空
        :return:
        """
        return self.cnt == 0

    def offer(self, val):
        """
        入队操作
        :param val:
        :return:
        """
        self.last.next = ListNode(val)
        self.last = self.last.next
        self.cnt += 1

    def poll(self):
        """
        出队操作
        :return:
        """
        if self.isEmpty():
            raise Empty("the queue is empty")
        if self.first.next == self.last:
            # 修改尾指针指向头指针
            self.last = self.first
        r = self.first.next
        self.first.next = r.next
        r.next = None
        self.cnt -= 1
        return r.val

    def peek(self):
        """
        获取队头元素
        :return:
        """
        if self.isEmpty():
            raise Empty("the queue is empty")
        r = self.first.next
        return r.val

    def size(self):
        """
        获取队列大小
        :return:
        """
        return self.cnt

    def __str__(self):
        vals = []
        head = self.first.next
        while head:
            vals.append(head.val)
            head = head.next
        return '->'.join(str(val) for val in vals)


class ArrayQueue:

    def __init__(self, n):
        self._vals = [None for _ in range(n)]
        self.cap = n
        self.first, self.last = 0, 0

    def isEmpty(self):
        return self.first == self.last

    def offer(self, val):
        if self.last == self.cap:
            raise Full('the queue is full')
        self._vals[self.last] = val
        self.last += 1

    def poll(self):
        if self.isEmpty():
            raise Empty('the queue is empty')
        r = self._vals[self.first]
        self.first += 1
        if self.first == self.last:
            self.first, self.last = 0, 0
        return r

    def peek(self):
        if self.isEmpty():
            raise Empty('the queue is empty')
        return self._vals[self.first]

    def size(self):
        return self.last - self.first

    def __str__(self):
        return str(self._vals)


class MyCircularQueue:
    """
    循环队列
    题目出处：https://leetcode.cn/problems/design-circular-queue/
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


class MyQueue:
    """
    使用栈实现队列
    题目出处：https://leetcode.cn/problems/implement-queue-using-stacks/description/
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if self.empty():
            raise Empty('the queue is empty')
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.empty():
            raise Empty('the queue is empty')
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


if __name__ == '__main__':
    # q = LinkedQueue()
    # print(q.isEmpty())
    # for i in range(10):
    #     q.offer(i)
    # print(q)
    # print(q.size())
    # for i in range(10):
    #     assert q.peek() == i
    #     assert q.poll() == i
    # print(q.isEmpty())
    # print(q.first.next is None)
    # print(q.first is q.last)
    # q.offer(100)
    # print(q.size())
    # print(q)
    q = ArrayQueue(10)
    print(q.isEmpty())
    for i in range(10):
        q.offer(i)
    print(q)
    print(q.size())
    for i in range(10):
        assert q.peek() == i
        assert q.poll() == i
    print(q.isEmpty())
    q.offer(100)
    print(q.size())
    print(q)
