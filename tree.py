class BSTree:

    class TreeNode:

        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self) -> None:
        self._root = None

    def insert(self, val):
        def _insert(root, val):
            if root is None:
                return type(self).TreeNode(val)
            # 根据二叉搜索树的定义：左子树的所有节点的值都比根节点的值小
            if val < root.val:
                root.left = _insert(root.left, val)
            elif val > root.val:
                root.right = _insert(root.right, val)
            else:
                # 严格定义的二叉搜索树中不允许有相同的值
                raise ValueError(f"val: {val} must lt or gt root.val: {root.val}")
            return root
        self._root = _insert(self._root, val)
    
    def _get_min_value(self, root):
        while root and root.left is not None:
            root = root.left
        return root.val

    def remove(self, val):
        def _remove(root, val):
            if root is None:
                return None
            if val < root.val:
                root.left = _remove(root.left, val)
            elif val > root.val:
                root.right = _remove(root.right, val)
            else:
                # 删除的是根节点
                # 如果左子树是空子树
                if root.left is None:
                    right = root.right
                    root = None
                    return right
                elif root.right is None:
                    left = root.left
                    root = None
                    return left
                else:
                    minValue = self._get_min_value(root.right)
                    root.val = minValue
                    root.right = _remove(root.right, minValue)
            return root
        self._root = _remove(self._root, val)


# class TrieTree:

#     class TrieNode:

#         def __init__(self) -> None:
#             self.path = 0
#             self.end = 0
#             self.nexts = [None for i in range(26)]
            
    
#     def __init__(self) -> None:
#         self._root = type(self).TrieNode()

#     def insert(self, word: str):
#         """将字符串 word 插入前缀树中
#         """
#         root = self._root
#         root.path += 1
#         for i in range(len(word)):
#             j = ord(word[i]) - ord('a')
#             if root.nexts[j] is None:
#                 root.nexts[j] = type(self).TrieNode()
#             root = root.nexts[j]
#             root.path += 1
#         root.end += 1

#     def search(self, word: str):
#         """返回前缀树中字符串 word 的实例个数
#         """
#         root = self._root
#         for i in range(len(word)):
#             j = ord(word[i]) - ord('a')
#             if root.nexts[j] is None:
#                 return 0
#             root = root.nexts[j]
#         return root.end
    
#     def prefix(self, p):
#         """返回前缀树中以 p 为前缀的字符串个数
#         """
#         root = self._root
#         for i in range(len(p)):
#             j = ord(p[i]) - ord('a')
#             if root.nexts[j] is None:
#                 return 0
#             root = root.nexts[j]
#         return root.path
        
    
#     def delete(self, word):
#         """从前缀树中移除字符 word
#         """
#         if self.search(word) > 0:
#             root = self._root
#             root.path -= 1
#             for i in range(len(word)):
#                 j = ord(word[i]) - ord('a')
#                 root.nexts[j].path -= 1
#                 if root.nexts[j].path == 0:
#                     root.nexts[j] = None
#                     return
#                 root = root.nexts[j]
#             root.end -= 1


class TrieTree:

    def __init__(self) -> None:
        self._N = 150001
        self._tree = [[0 for i in range(26)] for j in range(self._N)]
        self._end = [0 for i in range(self._N)]
        self._path = [0 for i in range(self._N)]
        self._cnt = 1
    
    def rebuild(self):
        for i in range(self._cnt):
            for j in range(26):
                self._tree[i][j] = 0
            self._end[i] = 0
            self._path[i] = 0
        self._cnt = 1
    
    def insert(self, word):
        cur = 1
        self._path[cur] += 1
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if self._tree[cur][j] == 0:
                self._cnt += 1
                self._tree[cur][j] = self._cnt
            cur = self._tree[cur][j]
            self._path[cur] += 1
        self._end[cur] += 1
    
    def search(self, word):
        cur = 1
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if self._tree[cur][j] == 0:
                return 0
            cur = self._tree[cur][j]
        return self._end[cur]
    
    def prefix(self, p):
        cur = 1
        for i in range(len(p)):
            j = ord(p[i]) - ord('a')
            if self._tree[cur][j] == 0:
                return 0
            cur = self._tree[cur][j]
        return self._path[cur]
    
    def delete(self, word):
        if self.search(word) > 0:
            cur = 1
            for i in range(len(word)):
                j = ord(word[i]) - ord('a')
                self._path[self._tree[cur][j]] -= 1
                if self._path[self._tree[cur][j]] == 0:
                    self._tree[cur][j] = 0
                    return
                cur = self._tree[cur][j]
            self._end[cur] -= 1


class AVLTree:

    class TreeNode:

        def __init__(self, val) -> None:
            self.val = val
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self) -> None:
        pass

    def insert(self, val):
        pass

    def remove(self, val):
        pass
