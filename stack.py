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
    
    def sort(self):
        """时间复杂度：O(N^2)
        """
        def _sort(stack):
            d = deep(stack)
            while d > 0:
                maxValue = MAX(stack, d)
                k = times(stack, d, maxValue)
                down(stack, d, maxValue, k)
                d -= k
            
        def deep(stack):
            """利用递归求栈的深度
            """
            if len(stack) == 0:
                return 0
            top = stack.pop()
            ret = deep(stack) + 1
            stack.append(top)
            return ret

        def MAX(stack, deep):
            """利用递归查找栈中的最大值
            """
            if deep == 0:
                return -2 ** 31
            num = stack.pop()
            ret = max(num, MAX(stack, deep - 1))
            stack.append(num)
            return ret
        
        def times(stack, d, maxValue):
            """利用递归统计栈中最大值出现的次数
            """
            ret = 0
            if d == 0:
                return ret
            num = stack.pop()
            ret += 1 if num == maxValue else 0
            ret += times(stack, d - 1, maxValue)
            stack.append(num)
            return ret
        
        def down(stack, d, maxValue, k):
            """利用递归将栈中的最大值下沉到栈底
            """
            if d == 0:
                while k:
                    stack.append(maxValue)
                    k -= 1
                return
            num = stack.pop()
            down(stack, d - 1, maxValue, k)
            if num != maxValue:
                stack.append(num)
            return
        _sort(self._vals)


class LinkedStack:

    class ListNode:

        def __init__(self, val, next=None):
            self.next = next
            self.val = val

    def __init__(self):
        self._size = 0
        self.top = type(self).ListNode(None)
    
    def push(self, val):
        n = type(self).ListNode(val)
        n.next = self.top.next
        self.top.next = n
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty('the stack is empty')
        top = self.top.next
        self.top.next = top.next
        self._size -= 1
        return top.val

    def top(self):
        if self._size == 0:
            raise Empty('the stack is empty')
        top = self.top.next
        return top.val

    def size(self):
        return self._size

    def __str__(self):
        vals = []
        head = self.top.next
        while head:
            vals.append(head.val)
            head = head.next
        vals.reverse()
        return '->'.join(str(val) for val in vals)


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
