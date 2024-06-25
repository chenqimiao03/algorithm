# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        import collections
        deque = collections.deque()
        result = []
        deque.append(root)
        while deque:
            size = len(deque)
            temp = []
            # 一次处理一层
            for _ in range(size):
                node = deque.popleft()
                if node.left != None:
                    deque.append(node.left)
                if node.right != None:
                    deque.append(node.right)
                temp.append(node.val)
            result.append(temp)
        return result
