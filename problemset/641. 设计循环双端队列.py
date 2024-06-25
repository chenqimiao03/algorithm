class Deque:
    """
    使用固定数组实现双端队列（也可以使用双向链表实现）
    验证链接：https://leetcode.cn/problems/design-circular-deque/
    """

    def __init__(self, n):
        self.cap = n
        self.d = [None for _ in range(n)]
        self.left, self.right, self.size = 0, 0, 0

    def insertFront(self, value):
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.left, self.right = 0, 0
                self.d[0] = value
            else:
                self.left = self.cap - 1 if self.left == 0 else self.left - 1
                self.d[self.left] = value
            self.size += 1
            return True

    def insertLast(self, value):
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.left, self.right = 0, 0
                self.d[0] = value
            else:
                self.right = 0 if self.right == self.cap - 1 else self.right + 1
                self.d[self.right] = value
            self.size += 1
            return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        else:
            self.left = 0 if self.left == self.cap - 1 else self.left + 1
            self.size -= 1
            return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        else:
            self.right = self.cap - 1 if self.right == 0 else self.right - 1
            self.size -= 1
            return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.d[self.left]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.d[self.right]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.cap
