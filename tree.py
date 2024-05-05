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


def preorderTraversal_non_recur(root: TreeNode):
    """
    二叉树的先序遍历（非递归）
    :param root:
    :return:
    """
    ret = []
    if root is not None:
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            ret.append(root.val)
            # 因为栈的特性（后进先出）所以要先判断右子树
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
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


def inorderTraversal_non_recur(root: TreeNode):
    """
    二叉树的中序遍历（非递归）
    :param root:
    :return:
    """
    ret = []
    stack = []
    if root is not None:
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                # 一直找到最左边的孩子
                root = root.left
            else:
                root = stack.pop()
                ret.append(root.val)
                root = root.right
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


def postorderTraversal_non_recur(root: TreeNode):
    """
    二叉树的后序遍历（非递归）
    :param root:
    :return:
    """
    ret = []
    if root is not None:
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            # 遍历顺序变为：根右左
            root = stack1.pop()
            stack2.append(root)
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        # 对所有节点做一个逆序处理就变成了左右根
        while stack2:
            ret.append(stack2.pop().val)
    return ret
