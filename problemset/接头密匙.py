#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param b int整型二维数组 
# @param a int整型二维数组 
# @return int整型一维数组
#
class TrieTree:

    def __init__(self) -> None:
        self._N = 80001
        self._tree = [[0 for i in range(12)] for j in range(self._N)]
        self._path = [0 for i in range(self._N)]
        self._cnt = 1
    
    def build(self):
        self._cnt = 1
    
    def charAt(self, c):
        if c == '-':
            return 10
        elif c == '#':
            return 11
        else:
            return ord(c) - ord('0')
    
    def clear(self):
        for i in range(self._cnt):
            for j in range(12):
                self._tree[i][j] = 0
            self._path[i] = 0
        self._cnt = 1
    
    def insert(self, word):
        cur = 1
        self._path[cur] += 1
        for i in range(len(word)):
            j = self.charAt(word[i])
            if self._tree[cur][j] == 0:
                self._cnt += 1
                self._tree[cur][j] = self._cnt
            cur = self._tree[cur][j]
            self._path[cur] += 1
    
    def count(self, word):
        cur = 1
        for i in range(len(word)):
            j = self.charAt(word[i])
            if self._tree[cur][j] == 0:
                return 0
            cur = self._tree[cur][j]
        return self._path[cur]


class Solution:
    def countConsistentKeys(self , b: List[List[int]], a: List[List[int]]) -> List[int]:
        # write code here
        tree = TrieTree()
        tree.build()
        for num in a:
            builder = []
            for i in range(1, len(num)):
                builder.append(str(num[i] - num[i - 1]))
                builder.append('#')
            tree.insert(''.join(builder))
        ret = []
        for i in range(len(b)):
            builder = []
            for j in range(1, len(b[i])):
                builder.append(str(b[i][j] - b[i][j - 1]))
                builder.append('#')
            ret.append(tree.count(''.join(builder)))
        tree.clear()
        return ret


