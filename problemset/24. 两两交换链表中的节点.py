# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None)
        prev.next = head
        result = prev
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            prev.next, a.next, b.next = b, b.next, a
            prev = a
        return result.next