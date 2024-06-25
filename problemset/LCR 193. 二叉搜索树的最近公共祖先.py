# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """二叉搜索树（不包含重复值）：每个节点左子树中的值 < 根节点的值 < 右子树中的值，并且每棵子树都要符合该性质
        1. 当前节点的值比 q 和 p 的最小值还小，那就去右子树中找
        2. 当前节点的值比 q 和 p 的最大值还大，那就去左子树中找
        3. 当前节点的值在 q 和 p 两个节点之间，那么当前节点就是最近公共祖先
        4. 先遇到哪个节点，哪个节点就是最近公共祖先
        """
        while root.val != p.val and root.val != q.val:
            if min(p.val, q.val) < root.val and root.val < max(p.val, q.val):
                break
            root = root.right if root.val < min(p.val, q.val) else root.left
        return root
