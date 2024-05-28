"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    也可以使用哈希表来记录：{Node: Node'}
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        tail = head
        while tail:
            nxt = tail.next
            n = Node(tail.val)
            tail.next = n
            n.next = nxt
            tail = nxt
        tail = head
        # 复制 random 指针
        while tail:
            nxt = tail.next.next
            copy = tail.next
            # 如果当前节点的 random 域不为空
            if tail.random is not None:
                copy.random = tail.random.next
            tail = nxt
        # 拆分链表
        tail, ans = head, head.next
        while tail:
            nxt = tail.next.next
            copy = tail.next
            tail.next = nxt
            copy.next = nxt.next if nxt is not None else None
            tail = nxt
        return ans

