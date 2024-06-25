# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        nq = deque()
        iq = deque()
        nq.append(root)
        iq.append(1)
        ans = 1 # 节点数在 [1, 3000]
        while nq:
            ans = max(ans, iq[-1] - iq[0] + 1)
            size = len(nq)
            for _ in range(size):
                n = nq.popleft()
                i = iq.popleft()
                if n.left:
                    nq.append(n.left)
                    iq.append(2 * i)
                if n.right:
                    nq.append(n.right)
                    iq.append(2 * i + 1)
        return ans
