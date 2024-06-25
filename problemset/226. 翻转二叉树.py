# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invertTree(root):
            if root is None:
                return root
            root.left, root.right = _invertTree(root.right), _invertTree(root.left)
            return root
        return _invertTree(root)