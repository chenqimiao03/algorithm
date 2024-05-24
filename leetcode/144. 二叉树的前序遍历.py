# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    验证链接：https://leetcode.cn/problems/binary-tree-preorder-traversal/
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            stack = []
            ret = []
            stack.append(root)
            while stack:
                root = stack.pop()
                ret.append(root.val)
                # 因为栈的特性（后进先出）所以要先判断右子树
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
            return ret
        return []

    # def preorderTraversal(root: TreeNode):
    #     """
    #     二叉树的先序遍历（根左右）
    #     :param root:
    #     :return:
    #     """
    #     ret = []
    #     def _preorderTraversal(root):
    #         nonlocal ret
    #         if root is None:
    #             return None
    #         ret.append(root.val)
    #         _preorderTraversal(root.left)
    #         _preorderTraversal(root.right)
    #     _preorderTraversal(root)
    #     return ret
