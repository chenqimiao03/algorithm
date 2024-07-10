class DSU:

    def __init__(self, n=1000001) -> None:
        self._n = n
        # 构建指向自己的指针
        self._father = [i for i in range(n)]
        # 每个集合的大小
        self._size = [1 for i in range(n)]
        self._stack = [0 for i in range(n)]
        self._sets = n

    # i 号节点往上一直找，直到找到代表节点
    def find(self, i):
        size = 0
        while i != self._father[i]:
            self._stack[size] = i
            size += 1
            i = self._father[i]
        # 扁平化
        while size:
            self._father[self._stack[size - 1]] = i
            size -= 1
        return i

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            # 小挂大
            if self._size[fx] >= self._size[fy]:
                self._size[fx] += self._size[fy]
                self._father[fy] = fx
            else:
                self._size[fy] += self._size[fx]
                self._father[fx] = fy
            self._sets -= 1

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0]) # 都是异构词，长度都一样
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                if not dsu.isSameSet(i, j):
                    diff = 0
                    k = 0
                    while k < m and diff < 3:
                        if strs[i][k] != strs[j][k]:
                            diff += 1
                        k += 1
                    # diff=0：单词 strs[i] 和单词 strs[j] 相等
                    # diff=2：单词 strs[i] 在某个位置交换过 1 次
                    if diff == 0 or diff == 2:
                        dsu.union(i, j)
        return dsu._sets