class MyQueue:
    """
    验证链接：https://leetcode.cn/problems/implement-queue-using-stacks/
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if self.empty():
            raise Exception('the queue is empty')
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.empty():
            raise Exception('the queue is empty')
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
