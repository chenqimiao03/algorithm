# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    验证链接：https://leetcode.cn/problems/reverse-linked-list/description/
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, nxt = None, None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
