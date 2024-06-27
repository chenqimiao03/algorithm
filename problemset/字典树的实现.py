#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param operators string字符串二维数组 the ops
# @return string字符串一维数组
#

# class Trie:

#     def __init__(self) -> None:
#         self._N = 800001
#         self._tree = [[0 for i in range(26)] for j in range(self._N)]
#         self._end = [0 for i in range(self._N)]
#         self._path = [0 for i in range(self._N)]
#         self._cnt = 1
    
#     def rebuild(self):
#         for i in range(self._cnt):
#             for j in range(26):
#                 self._tree[i][j] = 0
#             self._end[i] = 0
#             self._path[i] = 0
#         self._cnt = 1
    
#     def insert(self, word):
#         cur = 1
#         self._path[cur] += 1
#         for i in range(len(word)):
#             j = ord(word[i]) - ord('a')
#             if self._tree[cur][j] == 0:
#                 self._cnt += 1
#                 self._tree[cur][j] = self._cnt
#             cur = self._tree[cur][j]
#             self._path[cur] += 1
#         self._end[cur] += 1
    
#     def search(self, word):
#         cur = 1
#         for i in range(len(word)):
#             j = ord(word[i]) - ord('a')
#             if self._tree[cur][j] == 0:
#                 return 0
#             cur = self._tree[cur][j]
#         return self._end[cur]
    
#     def prefix(self, p):
#         cur = 1
#         for i in range(len(p)):
#             j = ord(p[i]) - ord('a')
#             if self._tree[cur][j] == 0:
#                 return 0
#             cur = self._tree[cur][j]
#         return self._path[cur]
    
#     def delete(self, word):
#         if self.search(word) > 0:
#             cur = 1
#             for i in range(len(word)):
#                 j = ord(word[i]) - ord('a')
#                 self._path[self._tree[cur][j]] -= 1
#                 if self._path[self._tree[cur][j]] == 0:
#                     self._tree[cur][j] = 0
#                     return
#                 cur = self._tree[cur][j]
#             self._end[cur] -= 1

# class Solution:
#     def trieU(self , operators: List[List[str]]) -> List[str]:
#         # write code here
#         t = Trie()
#         ret = []
#         for o in operators:
#             if o[0] == '1':
#                 print("insert:", o[1])
#                 t.insert(o[1])
#             elif o[0] == '2':
#                 t.delete(o[1])
#             elif o[0] == '3':
#                 ret.append("YES" if t.search(o[1]) else "NO")
#             else:
#                 ret.append(str(t.prefix(o[1])))
#         return ret


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param operators string字符串二维数组 the ops
# @return string字符串一维数组
#
class Trie:

    class TrieNode:

        def __init__(self):
            self.nexts = {}
            self.path = 0
            self.end = 0

    def __init__(self):
        self._root = type(self).TrieNode()

    def insert(self, word: str) -> None:
        root = self._root
        root.path += 1
        for i in range(len(word)):
            if root.nexts.get(word[i]) is None:
                root.nexts[word[i]] = type(self).TrieNode()
            root = root.nexts[word[i]]
            root.path += 1
        root.end += 1

    def search(self, word: str) -> bool:
        root = self._root
        for i in range(len(word)):
            if root.nexts.get(word[i]) is None:
                return 0
            root = root.nexts[word[i]]
        return root.end

    def prefix(self, prefix: str) -> bool:
        root = self._root
        for i in range(len(prefix)):
            if root.nexts.get(prefix[i]) is None:
                return 0
            root = root.nexts[prefix[i]]
        return root.path
    
    def delete(self, word):
        if self.search(word) > 0:
            root = self._root
            for i in range(len(word)):
                root.path -= 1
                if root.path == 0:
                    root.nexts.pop(word[i])
                    return
                root = root.nexts[word[i]]
            root.end -= 1

class Solution:
    def trieU(self , operators: List[List[str]]) -> List[str]:
        # write code here
        t = Trie()
        ret = []
        for o in operators:
            if o[0] == '1':
                t.insert(o[1])
            elif o[0] == '2':
                t.delete(o[1])
            elif o[0] == '3':
                ret.append("YES" if t.search(o[1]) else "NO")
            else:
                ret.append(str(t.prefix(o[1])))
        return ret

