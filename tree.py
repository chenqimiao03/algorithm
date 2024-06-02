class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
用什么方式将二叉树序列化，就是用该方式将二叉树反序列化
中序遍历方式无法完成二叉树的序列化和反序列化，只有先序、后续和层序可以
"""