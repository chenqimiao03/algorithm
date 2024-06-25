# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        1. 如果 p 的子树中包含 q 那么这两个节点的最近公共祖先就是 p
        2. 如果 q 的子树中包含 p 那么这两个节点的最近公共祖先就是 q
        3. p 和 q 没有包含关系
        """
        if root is None or root is p or root is q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 两个节点在左右子树中
        if l is not None and r is not None:
            return root
        # 在左右子树中都搜索不到
        if l is None and r is None:
            return None
        return l if l is not None else r
