# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def _r(root):
            # 空树
            if root is None:
                return 0
            # 叶子节点
            if root.left is None and root.right is None:
                return 1
            l = float("inf")
            r = float("inf")
            # 当前节点不是叶子节点，并且有左子树
            if root.left is not None:
                l = _r(root.left)
            # 当前节点不是叶子节点，并且有右子树
            if root.right is not None:
                r = _r(root.right)
            return min(l, r) + 1
        return _r(root)