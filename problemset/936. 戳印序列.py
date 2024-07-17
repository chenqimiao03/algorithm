class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        # 以 indegree[i] 为开头长度为 n 的字符串和 stamp 有多少个对不上
        indegree = [n for i in range(m - n + 1)]
        graph = []
        for i in range(m):
            graph.append([])
        q = [0 for i in range(m - n + 1)]
        l, r = 0, 0
        for i in range(m - n + 1):
            # 以 i 开头长度为 n 的字符串
            for j in range(n):
                if target[i + j] == stamp[j]:
                    indegree[i] -= 1
                    # 如果入度为零，那说明是最后才盖上去的
                    if indegree[i] == 0:
                        q[r] = i
                        r += 1
                else:
                    graph[i + j].append(i)
        visited = [False for i in range(m)]
        path = [0 for i in range(m - n + 1)]
        size = 0
        while l < r:
            cur = q[l]
            l += 1
            path[size] = cur
            size += 1
            for i in range(n):
                if not visited[cur + i]:
                    visited[cur + i] = True
                    for nxt in graph[cur + i]:
                        indegree[nxt] -= 1
                        if indegree[nxt] == 0:
                            q[r] = nxt
                            r += 1
        if size != m - n + 1:
            return []
        i, j = 0, size - 1
        while i < j:
            path[i], path[j] = path[j], path[i]
            i += 1
            j -= 1
        return path