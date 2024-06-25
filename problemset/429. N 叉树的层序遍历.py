"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        if root is None:
            return ret
        from collections import deque
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            level = []
            for i in range(size):
                root = dq.popleft()
                level.append(root.val)
                for children in root.children:
                    dq.append(children)
            ret.append(level)
        return ret
