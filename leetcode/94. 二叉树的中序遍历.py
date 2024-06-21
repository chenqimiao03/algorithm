# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    验证链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = []
        if root is not None:
            while stack or root is not None:
                if root is not None:
                    stack.append(root)
                    # 一直找到最左边的孩子
                    root = root.left
                else:
                    root = stack.pop()
                    ret.append(root.val)
                    root = root.right
        return ret

    # def inorderTraversal(root: TreeNode):
    #     ret = []
    #     stack = []
    #     if root is not None:
    #         while stack or root is not None:
    #             if root is not None:
    #                 stack.append(root)
    #                 # 一直找到最左边的孩子
    #                 root = root.left
    #             else:
    #                 root = stack.pop()
    #                 ret.append(root.val)
    #                 root = root.right
    #     return ret