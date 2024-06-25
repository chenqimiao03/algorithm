# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # HASHSET = set()
        # while head:
        #     if head not in HASHSET:
        #         HASHSET.add(head)
        #     else:
        #         return True
        #     head = head.next
        # return False
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        if head is None or head.next is None:
            return False
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
        