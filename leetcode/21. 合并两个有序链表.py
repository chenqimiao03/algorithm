# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    验证链接：https://leetcode.cn/problems/merge-two-sorted-lists/
    """
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 is None or head2 is None:
            return head1 if head2 is None else head2
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
        return head.next
