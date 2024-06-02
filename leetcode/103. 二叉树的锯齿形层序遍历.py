# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrder(root):
            import collections
            if root == None:
                return list()
            dq = collections.deque()
            dq.append(root)
            levels = []
            reverse = False
            while dq:
                size = len(dq)
                level = []
                for i in range(size):
                    front = dq.popleft()
                    level.append(front.val)
                    if front.left:
                        dq.append(front.left)
                    if front.right:
                        dq.append(front.right)
                if reverse:
                    level.reverse()
                reverse = not reverse
                levels.append(level)
            return levels
        return levelOrder(root)
 