class BSTree:

    class TreeNode:

        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self) -> None:
        self._root = None

    def insert(self, val):
        pass

    def remove(self):
        pass

    def search(self):
        pass


# class Trie:

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


class Trie:

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
