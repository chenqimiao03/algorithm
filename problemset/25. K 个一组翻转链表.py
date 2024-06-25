# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    使用容器存储每个节点，然后在数组中按K个一组进行逆序
    验证链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        # 按照 K 个一组，进行分组
        for i in range(k):
            # 不足 K 个，保持原有顺序
            if tail == None:
                return head
            tail = tail.next
        result = None
        current = head
        while current != tail:
            temp = current.next
            current.next = result
            result = current
            current = temp
        head.next = self.reverseKGroup(tail, k)
        return result
