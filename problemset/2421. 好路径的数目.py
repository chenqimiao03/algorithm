"""并查集
"""
class DSU:

    def __init__(self, n=1000001) -> None:
        self._n = n
        # 构建指向自己的指针
        self._father = [i for i in range(n)]
        # 每个集合的大小
        self._size = [1 for i in range(n)]
        self._stack = [0 for i in range(n)]
        # 集合中最大值出现的次数
        self.maxValueCount = [1 for i in range(n)]

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

    # 谁的值大，谁就做代表节点
    def union(self, x, y, vals):
        fx = self.find(x)
        fy = self.find(y)
        # 好路径的条数
        path = 0
        if vals[fx] > vals[fy]:
            self._father[fy] = fx
            self._size[fx] += self._size[fy]
        elif vals[fx] < vals[fy]:
            self._father[fx] = fy
            self._size[fy] += self._size[fx]
        # 如果两个集合中的最大值一样
        else:
            path = self.maxValueCount[fx] * self.maxValueCount[fy]
            self._father[fy] = fx
            self._size[fx] += self._size[fy]
            self.maxValueCount[fx] += self.maxValueCount[fy]
        return path

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        dsu = DSU(30001)
        n = len(vals)
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        ret = n
        for edge in edges:
            ret += dsu.union(edge[0], edge[1], vals)
        return ret