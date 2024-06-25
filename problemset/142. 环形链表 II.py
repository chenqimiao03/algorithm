# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    验证链接：https://leetcode.cn/problems/linked-list-cycle-ii/description/
    """

    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        # 遍历链表，如果链表有环，那么在环内某处快慢指针必定相遇
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, self.hasCycle(head)
        if fast == None:
            return None
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
