# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        # 当前节点的值小于区间 [low, high] 的最小值
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 当前节点的值大于区间 [low, high] 的最大值
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 当前节点的值在区间 [low, high] 中
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root