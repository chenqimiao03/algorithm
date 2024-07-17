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
            return True
        return False

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)
