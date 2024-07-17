class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # favorite[i] = j, i -> j
        indegree = [0 for i in range(n)]
        for i in range(n):
            indegree[favorite[i]] += 1
        from collections import deque
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        # deep[i]：不包括 i 之内，i 之前所有路的最大长度
        deep = [0 for i in range(n)]
        # 只留下环
        while q:
            cur = q.popleft()
            nei = favorite[cur]
            deep[nei] = max(deep[nei], deep[cur] + 1)
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
        samll = 0 # 小环（只含两个节点的环）
        # 大环（包含3个及以上节点的环）
        # 因为环外的人最终喜欢的人都在环内，所以只能安排环内里的人数
        large = 0
        for i in range(n):
            if indegree[i] > 0:
                maxSize = 1
                indegree[i] = 0
                j = favorite[i]
                # 统计环中节点个数
                while j != i:
                    maxSize += 1
                    indegree[j] = 0
                    j = favorite[j]
                if maxSize == 2:
                    # 在喜欢我这条路上的深度
                    # 我喜欢的人有哪些人喜欢
                    samll += 2 + deep[i] + deep[favorite[i]]
                else:
                    large = max(maxSize, large)
        return max(large, samll)
