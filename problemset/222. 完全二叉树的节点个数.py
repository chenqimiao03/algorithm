# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """只适用完全二叉树
        """

        def height(cur, level):
            """
            """
            while cur:
                cur = cur.left
                level += 1
            return level - 1
        
        def f(cur, level, h):
            if level == h:
                return 1
            if height(cur.right, level + 1) == h:
                return (1 << (h - level)) + f(cur.right, level + 1, h)
            else:
                return (1 << (h - level - 1)) + f(cur.left, level + 1, h)
        if root is None:
            return 0
        return f(root, 1, height(root, 1))