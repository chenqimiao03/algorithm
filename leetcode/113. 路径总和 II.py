# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def process(h, target, current, path, ans):
            # 当前节点是叶子节点
            if h.left is None and h.right is None:
                if h.val + current == target:
                    path.append(h.val)
                    r = copy.deepcopy(path)
                    ans.append(r)
                    path.pop()
            # 不是叶子节点
            else:
                path.append(h.val)
                if h.left is not None:
                    process(h.left, target, current + h.val, path, ans)
                if h.right is not None:
                    process(h.right, target, current + h.val, path, ans)
                # 递归恢复现场
                path.pop()

        ans = []
        if root is not None:
            path = []
            process(root, targetSum, 0, path, ans)
        return ans