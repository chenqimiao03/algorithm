class MyStack:
    """
    验证链接：https://leetcode.cn/problems/implement-stack-using-queues/
    """

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if self.empty():
            raise Exception('the stack is empty')
        if len(self.q1):
            for i in range(len(self.q1)):
                self.q2.append(self.q1[i])
            self.q1 = []
        return self.q2.pop()

    def top(self):
        if self.empty():
            raise Exception('the stack is empty')
        if len(self.q1):
            for i in range(len(self.q1)):
                self.q2.append(self.q1[i])
            self.q1 = []
        return self.q2[-1]

    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()