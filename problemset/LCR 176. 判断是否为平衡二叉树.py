# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """平衡二叉树：对于每个节点，左子树的高度和右子树的高度之差小于等于 1
        """
        def height(root):
            nonlocal balance
            # 一旦发现不是平衡二叉树，返回什么高度都可以
            if not balance or root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh - rh) > 1:
                balance = False
            return max(lh, rh) + 1
        balance = True
        height(root)
        return balance