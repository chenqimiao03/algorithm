
class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = ListNode(None)

    def appendleft(self, val):
        n = ListNode(val)
        n.next = self.head.next
        self.head.next = n

    def popleft(self):
        ret = self.head.next
        if ret:
            self.head.next = ret.next
            ret.next = None
        return ret

    def reverse(self):
        """
        单链表反转
        题目出处：https://leetcode.cn/problems/reverse-linked-list/description/
        :return:
        """
        head = self.head.next
        pre, nxt = None, None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        self.head.next = pre

    def merge(self, other):
        """
        合并两个有序链表
        题目出处：https://leetcode.cn/problems/merge-two-sorted-lists/description/
        :param other:
        :return:
        """
        if self.head.next is None or other.head.next is None:
            return self.head.next if other.head.next is None else other.head.next
        head1, head2 = self.head.next, other.head.next
        head = ListNode(None)
        cur = head
        while head1 and head2:
            if head1.val >= head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        self.head.next = head.next

    def twosum(self, other):
        """
        两数相加
        题目出处：https://leetcode.cn/problems/add-two-numbers/
        :param other:
        :return:
        """
        if self.head.next is None or other.head.next is None:
            return self.head.next if other.head.next is None else other.head.next
        # 题目中不需要反转
        self.reverse()
        other.reverse()
        head1, head2 = self.head.next, other.head.next
        head = ListNode(None)
        carry, cur = 0, head
        while head1 or head2:
            SUM = (0 if head1 is None else head1.val) + (0 if head2 is None else head2.val) + carry
            cur.next = ListNode(SUM % 10)
            cur = cur.next
            carry = SUM // 10
            head1 = None if head1 is None else head1.next
            head2 = None if head2 is None else head2.next
        if carry:
            cur.next = ListNode(carry)
        return head.next

    def partition(self, x):
        """
        分割链表
        题目出处：https://leetcode.cn/problems/partition-list/
        :return:
        """
        left, right = ListNode(None), ListNode(None)
        cur1, cur2 = left, right
        head = self.head.next
        while head:
            nxt = head.next
            # 断开连接，如果不断开连接的话，需要在后面将 cur2 的 next 指向空
            head.next = None
            if head.val >= x:
                cur2.next = head
                cur2 = cur2.next
            else:
                cur1.next = head
                cur1 = cur1.next
            head = nxt
        # if cur2:
        #     cur2.next = None
        cur1.next = right.next
        self.head.next = left.next

    def __str__(self):
        vals = []
        head = self.head.next
        while head:
            vals.append(head.val)
            head = head.next
        return '->'.join(str(val) for val in vals)


def print_linkedlist(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print('->'.join(str(val) for val in vals))


if __name__ == '__main__':
    # l = LinkedList()
    # for i in range(10):
    #     l.appendleft(i)
    # print(l)
    # l.reverse()
    # print(l)
    # l1 = LinkedList()
    # l2 = LinkedList()
    # l1.appendleft(4)
    # l1.appendleft(2)
    # l1.appendleft(1)
    # l2.appendleft(4)
    # l2.appendleft(3)
    # l2.appendleft(1)
    # print(f'l1: {l1}')
    # print(f'l2: {l2}')
    # l1.merge(l2)
    # print(f'l1: {l1}')
    # l1 = LinkedList()
    # l2 = LinkedList()
    # l1.appendleft(9)
    # l1.appendleft(4)
    # l1.appendleft(2)
    # l2.appendleft(9)
    # l2.appendleft(4)
    # l2.appendleft(6)
    # l2.appendleft(5)
    # print(f'l1: {l1}')
    # print(f'l2: {l2}')
    # l1.reverse()
    # l2.reverse()
    # print(f'l1: {l1}')
    # print(f'l2: {l2}')
    # print_linkedlist(l1.twosum(l2))
    l = LinkedList()
    l.appendleft(2)
    l.appendleft(5)
    l.appendleft(2)
    l.appendleft(3)
    l.appendleft(4)
    l.appendleft(1)
    print(l)
    l.partition(3)
    print(l)

