# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    验证链接：https://leetcode.cn/problems/partition-list/
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(None), ListNode(None)
        cur1, cur2 = left, right
        while head:
            nxt = head.next
            # 断开连接，如果不断开连接的话，需要在后面将 cur2 的 next 指向空
            head.next = None
            if head.val >= x:
                cur2.next = head
                cur2 = head
            else:
                cur1.next = head
                cur1 = head
            head = nxt
        cur1.next = right.next
        return left.next
