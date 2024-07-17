class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 邻接表建图
        graph = []
        indegree = []
        for i in range(n + 1):
            graph.append([])
            indegree.append(0)
        for relation in relations:
            graph[relation[0]].append(relation[1])
            indegree[relation[1]] += 1
        from collections import deque
        dq = deque()
        for i in range(n + 1):
            if indegree[i] == 0:
                dq.append(i)
        # 完成第 i 件事所需要的时间
        cost = [0 for i in range(n + 1)]
        while dq:
            cur = dq.popleft()
            cost[cur] = cost[cur] + time[cur - 1]
            for nei in graph[cur]:
                if cost[cur] > cost[nei]:
                    cost[nei] = cost[cur]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dq.append(nei)
        return max(cost)