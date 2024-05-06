class MinStack:
    """
    验证链接：https://leetcode.cn/problems/min-stack/
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



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()