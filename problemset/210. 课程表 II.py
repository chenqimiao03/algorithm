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
    
    def __init__(self):
        # 点集和边集
        # 点集 该点的数据项: Vertex
        self.vertexs, self.edges = {}, set()
    
    def addVertex(self, val):
        # 如果图中不存在点 v 则添加
        if self.vertexs.get(val) == None:
            self.vertexs[val] = type(self).Vertex(val)
        return 
    
    def addEdge(self, frm, to, w=1):
        # 建立一条边
        new_edge = type(self).Edge(frm, to, w)
        # 从点集中取出 from 点
        frm = self.vertexs.get(frm)
        # 检查起点为 from 的所有边，如果存在这么一条边就更新其权值
        for edge in frm.edges:
            if edge.to == to:
                edge.weight = w
                return
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
    
    def Topological(self):
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
        return result if len(result) == len(self.vertexs) else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建图
        g = Graph()
        for i in range(numCourses):
            g.addVertex(i)
        for i in range(len(prerequisites)):
            g.addEdge(prerequisites[i][1], prerequisites[i][0])
        # 拓扑排序
        ret = g.Topological()
        return ret