# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def _r(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            # 根节点必定是先序遍历的第一个节点
            root = TreeNode(preorder[0])
            index = 0
            # 划分左右子树所包含的节点
            for i in range(len(inorder)):
                if inorder[i] == preorder[0]:
                    index = i
                    break
            left = _r(preorder[1: index+1], inorder[:index])
            right = _r(preorder[index+1:], inorder[index+1:])
            root.left = left
            root.right = right
            return root
        return _r(preorder, inorder)
