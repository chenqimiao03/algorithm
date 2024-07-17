class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        # 邻接表建图
        graph = []
        for i in range(n):
            graph.append([])
        indegree = [0 for i in range(n)]
        # r: [i, j] i 比 j 有钱
        for r in richer:
            graph[r[0]].append(r[1])
            indegree[r[1]] += 1
        from collections import deque
        dq = deque()
        for i in range(n):
            if indegree[i] == 0:
                dq.append(i)
        ret = []
        for i in range(n):
            ret.append(i)
        while dq:
            cur = dq.popleft()
            for nei in graph[cur]:
                # 向后传递消息
                if quiet[ret[nei]] > quiet[ret[cur]]:
                    ret[nei] = ret[cur]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dq.append(nei)
        return ret