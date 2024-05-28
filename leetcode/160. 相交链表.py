# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    验证链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        a, b, diff = headA, headB, 0
        while a:
            a = a.next
            diff += 1
        while b:
            b = b.next
            diff -= 1
        if a != b:
            return None
        if diff >= 0:
            a = headA
            b = headB
        else:
            a = headB
            b = headA
        diff = abs(diff)
        # 长链表先走差值步
        while diff:
            a = a.next
            diff -= 1
        # 如果两个链表相交，那么走到相交出就跳出循环，否则走到链表尾
        while a != b:
            a = a.next
            b = b.next
        return a