# class Graph:

#     def __init__(self, vertexes, vector=False) -> None:
#         # 邻接矩阵方式建图
#         # 不适合存储顶点太多的图
#         self._vertexes = vertexes
#         self._edges = [[0 for i in range(len(self._vertexes))] for j in range(len(self._vertexes))]
#         self._mapping = {v: k for k, v in enumerate(self._vertexes)}
#         # False：存储无向图，True：存储有向图
#         self._vector = vector

#     def add_edge(self, f, t, w=1):
#         if f not in self._mapping or t not in self._mapping:
#             raise ValueError(f'f or t must be in {self._mapping.keys()} but got: f: {f}, t: {t}')
#         i, j = self._mapping.get(f), self._mapping.get(t)
#         self._edges[i][j] = w # f - t
#         if not self._vector:
#             # t - f
#             self._edges[j][i] = w # 1：表示无权图
    
#     def __str__(self) -> str:
#         return str(self._edges)


# class Graph:
    
#     class LinkedList:

#         class ListNode:
        
#             def __init__(self, v, w=1, prev=None, next=None) -> None:
#                 self.next = next
#                 self.prev = prev
#                 self.v = v
#                 self.w = w

#         def __init__(self) -> None:
#             self.head = type(self).ListNode(None, None)
#             self.tail = type(self).ListNode(None, None)
#             self.head.next = self.tail
#             self.tail.prev = self.head
        
#         def append(self, t, w=1):
#             new_node = type(self).ListNode(t, w)
#             tail = self.head.next
#             tail.prev = new_node
#             new_node.next = tail
#             new_node.prev = self.head
#             self.head.next = new_node
        
#         def __str__(self) -> str:
#             head = self.head.next
#             result = []
#             while head is not self.tail:
#                 result.append("{" + f'vertex: {head.v}, weight: {head.w}' + "}")
#                 head = head.next
#             return ','.join(result)

#     def __init__(self, vertexes, vector=False) -> None:
#         # 邻接表方式建图
#         self._vertexes = vertexes
#         self._edges = [type(self).LinkedList() for i in range(len(self._vertexes))]
#         self._mapping = {v: k for k, v in enumerate(self._vertexes)}
#         # False：存储无向图，True：存储有向图
#         self._vector = vector
    
#     def add_edge(self, f, t, w=1):
#         if f not in self._mapping or t not in self._mapping:
#             raise ValueError(f'f or t must be in {self._mapping.keys()} but got: f: {f}, t: {t}')
#         i, j = self._mapping.get(f), self._mapping.get(t)
#         # f - t
#         self._edges[i].append(t, w)
#         if not self._vector:
#             # t - f
#             self._edges[j].append(f, w)
    
#     def __str__(self) -> str:
#         results = []
#         for vertex in self._vertexes:
#             i = self._mapping.get(vertex)
#             results.append(f'{vertex}: {str(self._edges[i])}\n')
#         return ''.join(results)


# class Graph:

#     def __init__(self, vertexes, edges, vector=False) -> None:
#         # 链式前向星方式建图（在固定数组上实现邻接表）
#         self._vertexes = vertexes
#         self._n_vertexes = len(self._vertexes) # 顶点个数
#         self._edges = edges
#         self._n_edges = len(self._edges) # 边的条数
#         self.head = [0 for i in range(self._n_vertexes)] # 顶点：该顶点最先处理的边，0 表示没有边可以继续处理了
#         self.NEXT, self.to, self.weight = [], [], []
#         for i in range(self._n_edges * 2):
#             self.NEXT.append(0) # 边的编号：该边的起点还有哪些边没有处理
#             self.to.append(0) # 边的编号：目标顶点
#             self.weight.append(0) # 边的编号：边的权值
#         self._v2i = {v: k for k, v in enumerate(self._vertexes)}
#         self._i2v = {k: v for k, v in enumerate(self._vertexes)}
#         self.count = 0 # 边的编号从 0 号开始
#         self._vector = vector
#         for edge in self._edges:
#             self.add_edge(edge[0], edge[1], edge[2])
#             if not self._vector:
#                 self.add_edge(edge[1], edge[0], edge[2])
    
#     def add_edge(self, f, t, w=1):
#         # f -> t 的边，权重为 w
#         i, j = self._v2i.get(f), self._v2i.get(t)
#         self.NEXT[self.count] = self.head[i] # 以 f 为起点的边有哪些
#         self.to[self.count] = j # 现在这一条边去往哪里的
#         self.weight[self.count] = w # 现在这一条边的权重值
#         self.head[i] = self.count # 以 f 为起点的边，最先处理的就是编号为 count 的边
#         self.count += 1
    
#     def __str__(self) -> str:
#         result = []
#         for vertex in self._vertexes:
#             i = self._v2i.get(vertex)
#             e = self.head[i]
#             result.append(f'{vertex}: ')
#             # 还有边没有处理
#             while e > 0:
#                 result.append("{" + f'vertex: {self._i2v.get(self.to[e])}, weight: {self.weight[e]}' + "}")
#                 e = self.NEXT[e]
#             result.append('\n')
#         return ''.join(result)


class Graph:
    
    class Vertex:
        
        def __init__(self, val):
            # 该点的数据项，比如说 0 号城市的 val 就是 0，A 号城市的数据项就是 A
            self.Val = val
            # 该点的入度和出度
            self.In, self.Out = 0, 0
            # 该点的直接邻居点和以该点为起点的边
            self.nexts, self.edges = [], []
        
        def __repr__(self):
            vertexs = []
            # 打印其邻居
            for edge in self.edges:
                vertexs.append(edge.to)
            return '->'.join(vertexs)
    
    class Edge:
        
        def __init__(self, frm, to, weight):
            self.weight, self.frm, self.to = weight, frm, to

        def __gt__(self, o):
            return self.weight > o.weight
        
        def __lt__(self, o):
            return self.weight < o.weight
    
    def __init__(self, vector=False):
        # 点集、边集和有向图还是无向图
        # 点集 该点的数据项: Vertex
        self.vertexs, self.edges, self.vector = {}, set(), vector
    
    def add_vertex(self, val):
        # 如果图中不存在点 v 则添加
        if self.vertexs.get(val, None) is None:
            self.vertexs[val] = type(self).Vertex(val)
        return 
    
    def add_edge(self, frm, to, w):
        def _add_edge(frm, to, w):
            new_edge = type(self).Edge(frm, to, w)
            # 从点集中取出 from 点
            frm = self.vertexs.get(frm)
            # 从点集中取出 to 点
            to = self.vertexs.get(to)
            # 将点 to 加到 from 的邻居中
            frm.nexts.append(to)
            # 将边加入到 from 点的边集中
            frm.edges.append(new_edge)
            # from 的出度加 1
            frm.Out += 1
            # to 的入度加 1
            to.In += 1
            self.edges.add(new_edge)
        _add_edge(frm, to, w)
        if not self.vector:
            _add_edge(to, frm, w)
    
    def Topological(self):
        # 无向图
        if not self.vector:
            return "exists ring"
        # 拓扑排序
        import collections
        HashMap = {} # 顶点: 当前顶点的剩余入度
        # 当某个点的入度为 0 时将其加入到队列中
        dq = collections.deque()
        for val, vertex in self.vertexs.items():
            HashMap[val] = vertex.In
            if vertex.In == 0:
                dq.append(val)
        # 拓扑排序的结果
        result = []
        while dq:
            front = dq.popleft()
            result.append(front)
            for vertex in self.vertexs.get(front).nexts:
                # 将邻居的入度减 1
                HashMap[vertex.Val] = HashMap[vertex.Val] - 1
                if HashMap[vertex.Val] == 0:
                    dq.append(vertex.Val)
        return result if len(result) == len(self.vertexs) else "exists ring"

    def kruskal(self):
        # kruskal 也可以不用建图
        from dsu import DSU
        n = len(self.vertexs)
        DisjointSet = DSU(n)
        keys = list(self.vertexs.keys())
        mapping = {keys[i]: i for i in range(n)}
        edges = list(self.edges)
        # 边根据权重排序
        edges.sort()
        result = 0 # 最小生成树的权重
        count = 0 # 最小生成树的边数
        for edge in edges:
            if DisjointSet.union(mapping.get(edge.frm), mapping.get(edge.to)):
                result += edge.weight
                count += 1
        # n 个节点的最小生成必然有 n - 1 条边
        return result if count == n - 1 else "orz"
    
    def prim(self):
        # 时间复杂度：O(N + M) + O(M * log(M))
        from random import choice
        from heap import Heap
        HashSet = set()
        n = len(self.edges)
        h = Heap(n, cmp=lambda a, b: a < b)
        vertex = choice(list(self.vertexs.values())) # 从点集中随机取出一点
        for edge in vertex.edges:
            h.heappush(edge)
        count = 1
        result = 0
        HashSet.add(vertex.Val)
        while not h.empty():
            edge = h.heappop()
            to = edge.to
            if to not in HashSet:
                HashSet.add(to)
                count += 1
                result += edge.weight
                for e in self.vertexs.get(to).edges:
                    h.heappush(e)
        return result if count == len(self.vertexs) else "orz"

    def __repr__(self):
        for k, v in self.vertexs.items():
            print(f'vertex: {k}, neighbor: {v}')
        return 'OK'