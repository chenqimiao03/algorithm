class LinkedList:

    class ListNode:

        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = type(self).ListNode(None)

    def appendleft(self, val):
        n = type(self).ListNode(val)
        n.next = self.head.next
        self.head.next = n

    def popleft(self):
        ret = self.head.next
        if ret:
            self.head.next = ret.next
            ret.next = None
        return ret

    def __str__(self):
        vals = []
        head = self.head.next
        while head:
            vals.append(head.val)
            head = head.next
        return '->'.join(str(val) for val in vals)


if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.appendleft(i)
    print(l)
