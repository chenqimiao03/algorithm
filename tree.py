class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode):
    """
    二叉树的先序遍历（根左右）
    题目出处：https://leetcode.cn/problems/binary-tree-preorder-traversal/
    :param root:
    :return:
    """
    ret = []
    def _preorderTraversal(root):
        nonlocal ret
        if root is None:
            return None
        ret.append(root.val)
        _preorderTraversal(root.left)
        _preorderTraversal(root.right)
    _preorderTraversal(root)
    return ret


def inorderTraversal(root: TreeNode):
    """
    二叉树的中序遍历（左根右）
    题目出处：https://leetcode.cn/problems/binary-tree-inorder-traversal/
    :param root:
    :return:
    """
    ret = []
    def _inorderTraversal(root):
        nonlocal ret
        if root is None:
            return None
        _inorderTraversal(root.left)
        ret.append(root.val)
        _inorderTraversal(root.right)
    _inorderTraversal(root)
    return ret


def postorderTraversal(root: TreeNode):
    """
    二叉树的后序遍历（左右根）
    题目出处：https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
    :param root:
    :return:
    """
    ret = []
    def _postorderTraversal(root):
        nonlocal ret
        if root is None:
            return None
        _postorderTraversal(root.left)
        _postorderTraversal(root.right)
        ret.append(root.val)
    _postorderTraversal(root)
    return ret
