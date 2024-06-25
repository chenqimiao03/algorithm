# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root is not None:
            stack = []
            stack.append(root)
            # root 的含义：上一次打印的节点
            while stack:
                cur = stack[-1]
                # 当前节点有左子树并且左子树没有被处理过
                if cur.left is not None and cur.left is not root and cur.right is not root:
                    stack.append(cur.left)
                # 当前节点有右子树并且右子树没有被处理过
                elif cur.right is not None and root != cur.right:
                    stack.append(cur.right)
                # 没有左右子树或者左右子树都被处理过了
                else:
                    ret.append(cur.val)
                    root = stack.pop()
        return ret

    # def postorderTraversal(root: TreeNode):
    #     ret = []
    #     def _postorderTraversal(root):
    #         nonlocal ret
    #         if root is None:
    #             return None
    #         _postorderTraversal(root.left)
    #         _postorderTraversal(root.right)
    #         ret.append(root.val)
    #     _postorderTraversal(root)
    #     return ret

    # def postorderTraversal(root: TreeNode):
    #     ret = []
    #     if root is not None:
    #         stack1 = []
    #         stack2 = []
    #         stack1.append(root)
    #         while stack1:
    #             # 遍历顺序变为：根右左（参考非递归的先序遍历）
    #             root = stack1.pop()
    #             stack2.append(root)
    #             if root.left:
    #                 stack1.append(root.left)
    #             if root.right:
    #                 stack1.append(root.right)
    #         # 对所有节点做一个逆序处理就变成了左右根
    #         while stack2:
    #             ret.append(stack2.pop().val)
    #     return ret