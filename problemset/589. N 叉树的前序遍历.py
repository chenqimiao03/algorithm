"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        def _preorder(root):
            nonlocal ret
            if root is None:
                return
            ret.append(root.val)
            for children in root.children:
                _preorder(children)
        _preorder(root)
        return ret