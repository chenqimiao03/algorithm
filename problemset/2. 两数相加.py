# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    """
    单链表反转
    题目出处：https://leetcode.cn/problems/reverse-linked-list/description/
    :return:
    """
    pre, nxt = None, None
    while head:
        nxt = head.next
        head.next = pre
        pre = head
        head = nxt
    return pre


class Solution:
    """
    验证链接：https://leetcode.cn/problems/add-two-numbers/
    """

    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        # 942 + 9465
        if head1 is None or head2 is None:
            return head1 if head2 is None else head2
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
