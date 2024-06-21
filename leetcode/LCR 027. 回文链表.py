# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    验证链接：https://leetcode.cn/problems/aMhZSa/description/
    """
    def isPalindrome(self, head: ListNode) -> bool:
        # stack = []
        # while head :
        #     stack.append(head.val)
        #     head = head.next
        # i, j = 0, len(stack) - 1
        # while i < j:
        #     if stack[i] != stack[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        # 快慢指针：快指针每次走两步，慢指针每次走一步
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow:
            n = slow.next
            slow.next = pre
            pre = slow
            slow = n
        left, right = head, pre
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
