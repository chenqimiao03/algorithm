# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    用什么方式将二叉树序列化，就是用该方式将二叉树反序列化
    中序遍历方式无法完成二叉树的序列化和反序列化，只有先序、后续和层序可以
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # 先序遍历二叉树
        def preorderTraversal(root):
            nonlocal result
            if root == None:
                # 空结点使用 # 符号来代替
                result.append('#')
                return
            result.append(str(root.val))
            result.append('!')  # 结点与结点的分割符
            preorderTraversal(root.left)
            preorderTraversal(root.right)

        result = []
        if root == None:
            return '#'
        preorderTraversal(root)
        return ''.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index = 0

        def _decode():
            nonlocal index
            if data[index] == '#':
                index += 1
                return None
            val = 0
            toggle = True
            while data[index] != '!' and index < len(data):
                if data[index] == '-':
                    toggle = False
                else:
                    val = val * 10 + (ord(data[index]) - ord('0'))
                index = index + 1
            if not toggle:
                val = -val
            root = TreeNode(val)
            if index >= len(data):
                return root
            else:
                index = index + 1
            root.left = _decode()
            root.right = _decode()
            return root

        if data == '#':
            return None
        return _decode()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))