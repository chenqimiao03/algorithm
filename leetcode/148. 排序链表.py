# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(pHead1, pHead2):
            result = ListNode(None)
            current = result
            while pHead1 and pHead2:
                if pHead1.val > pHead2.val:
                    current.next = pHead2
                    pHead2 = pHead2.next
                else:
                    current.next = pHead1
                    pHead1 = pHead1.next
                current = current.next
            current.next = pHead1 if pHead1 else pHead2
            return result.next

        def mergeSort(head):
            if head is None or head.next is None:
                return head
            left, mid, right = head, head.next, head.next.next
            # 找到链表的中点
            while right and right.next:
                left = left.next
                mid = mid.next
                right = right.next.next
            left.next = None
            return merge(mergeSort(head), mergeSort(mid))
        return mergeSort(head)
