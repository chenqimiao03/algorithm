"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        def _postorder(root):
            nonlocal ret
            if root is None:
                return
            for children in root.children:
                _postorder(children)
            ret.append(root.val)
        _postorder(root)
        return ret