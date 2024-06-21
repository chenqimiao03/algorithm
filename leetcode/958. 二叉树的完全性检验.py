# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        完全二叉树的定义：
        1. 满二叉树是完全二叉树
        2. 如果某一层的节点不满的话，那么节点是从左往右排列的
        验证方法：
        1. 如果有右孩子没有左孩子，那么这棵树就不是完全二叉树
        2. 如果遇到孩子不全的节点，接下来的节点不都是叶子节点，那么这棵树就不是完全二叉树
        """
        import collections
        dq = collections.deque()
        if root is None:
            return True
        dq.append(root)
        leaf = False
        while dq:
            root = dq.popleft()
            if (root.left is None and root.right) or (leaf and (root.left or root.right)):
                return False
            if root.left:
                dq.append(root.left)
            if root.right:
                dq.append(root.right)
            if root.left is None  or root.right is None:
                leaf = True
        return True