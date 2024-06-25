# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 在偷根节点的情况下，最大的收益
        yes = 0
        # 在不偷根节点的情况下，最大的收益
        no = 0
        def _rob(root):
            nonlocal yes, no
            f(root)
            return max(yes, no)

        def f(root):
            nonlocal yes, no
            # 空树偷不偷收益都是 0
            if root is None:
                yes = 0
                no = 0
            else:
                # 偷当前节点
                y = root.val
                # 不偷当前节点
                n = 0
                # 左子树不偷当前节点的左孩子的最好收益，在 yes 和 no 这两个变量中记录
                f(root.left)
                # 如果当前节点采取的方案是偷的话，就和左子树中的 no（不偷当前节点的左孩子） 相加
                y += no
                # 如果当前节点采取的方案是不偷的话，就和 yes（偷左孩子） 和 no（不偷左孩子） 的最大值相加
                n += max(yes, no)
                f(root.right)
                y += no
                n += max(yes, no)
                # 更新全局变量
                yes = y
                no = n
        return _rob(root)
