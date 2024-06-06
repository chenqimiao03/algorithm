# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        1. 中序遍历二叉搜索树得到一个严格递增的序列
        2. 验证每个节点是否满足二叉搜索树的定义
        """
        # nodes = []
        # def _r(root):
        #     nonlocal nodes
        #     if root == None:
        #         return
        #     _r(root.left)
        #     nodes.append(root.val)
        #     _r(root.right)
        # _r(root)
        # for i in range(1, len(nodes)):
        #     if nodes[i] <= nodes[i-1]:
        #         return False
        # return True
        minValue = float("inf")
        maxValue = float("-inf")
        def _isValidBST(root):
            nonlocal minValue, maxValue
            if root is None:
                minValue = float("inf")
                maxValue = float("-inf")
                return True
            lok = _isValidBST(root.left)
            lmin = minValue
            lmax = maxValue
            rok = _isValidBST(root.right)
            rmin = minValue
            rmax = maxValue
            minValue = min(lmin, rmin, root.val)
            maxValue = max(lmax, rmax, root.val)
            return lok and rok and lmax < root.val and root.val < rmin
        return _isValidBST(root)
        