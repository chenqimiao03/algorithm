class Solution:

    def build(self, initial, n):
        self._father = [i for i in range(n)]
        # 每个集合中有多少个节点
        self._size = [1 for i in range(n)]
        # 每个集合的标签（感染点：-1 表示无感染点，-2 表示有两个及以上的感染点，大于等于 0 表示感染点的位置）
        self._infect = [-1 for i in range(n)]
        # 快速定位第 i 个节点是不是带有病毒的节点
        self._virus = [False for i in range(n)]
        # 统计删除这个病毒节点能让多少个节点避免感染病毒
        self._cnts = [0 for i in range(n)]
        for i in initial:
            self._virus[i] = True
    
    def find(self, i):
        # i 号节点往上一直找，直到找到代表节点
        if i != self._father[i]:
            self._father[i] = self.find(self._father[i])
        return self._father[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self._size[fy] += self._size[fx]
            self._father[fx] = fy

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        self.build(initial, n)
        for i in range(n):
            for j in range(n):
                # 普通节点
                if graph[i][j] == 1 and not self._virus[i] and not self._virus[j]:
                    self.union(i, j)
        for i in initial:
            for nei in range(n):
                # 当前的邻居不是我自己
                # 当前的邻居也不是病毒点
                # 真的和普通节点存在连接
                if i != nei and not self._virus[nei] and graph[i][nei] == 1:
                    fn = self.find(nei)
                    if self._infect[fn] == -1:
                        # 当前的节点没有被感染过
                        self._infect[fn] = i
                    # 存在两个感染点
                    elif self._infect[fn] != -2 and self._infect[fn] != i:
                        self._infect[fn] = -2
        for i in range(n):
            # 该区域内存在一个病毒点
            if i == self.find(i) and self._infect[i] >= 0:
                self._cnts[self._infect[i]] += self._size[i]
        initial.sort()
        ret = initial[0]
        for i in initial:
            if self._cnts[i] > self._cnts[ret]:
                ret = i
        return ret