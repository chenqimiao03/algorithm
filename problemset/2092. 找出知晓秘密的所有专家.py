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
        # 集合标签信息（集合的代表元素中）
        self._secret = [False for i in range(n)]
        # 第 0 号专家直到秘密
        self._secret[0] = True

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
                # 将 fy 的代表节点设置成 fx
                self._father[fy] = fx
                self._secret[fx] |= self._secret[fy]
            else:
                self._size[fy] += self._size[fx]
                self._father[fx] = fy
                self._secret[fy] |= self._secret[fx]

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)
    
    def earse(self, i):
        self._father[i] = i
    
    def getSecret(self, i):
        return self._secret[i]


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        dsu = DSU(100001)
        dsu.union(firstPerson, 0)
        m = len(meetings)
        l = 0
        while l < m:
            r = l
            # 统计相同时刻有多少场会议
            while r + 1 < m and meetings[l][2] == meetings[r + 1][2]:
                r += 1
            # 在一起开会的专家都在一个集合中
            for i in range(l, r + 1):
                dsu.union(meetings[i][0], meetings[i][1])
            for i in range(l, r + 1):
                a, b = meetings[i][0], meetings[i][1]
                if not dsu.getSecret(dsu.find(a)):
                    dsu.earse(a)
                if not dsu.getSecret(dsu.find(b)):
                    dsu.earse(b)
            l = r + 1
        ret = []
        for i in range(n):
            # 代表节点是否知道秘密
            if dsu.getSecret(dsu.find(i)):
                ret.append(i)
        return ret