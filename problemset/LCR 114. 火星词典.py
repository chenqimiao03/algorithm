class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = [-1 for i in range(26)]
        for w in words:
            for c in w:
                indegree[ord(c) - ord('a')] = 0
        graph = []
        for i in range(26):
            graph.append([])
        for i in range(len(words) - 1):
            cur = words[i]
            NEXT = words[i + 1]
            j = 0
            length = min(len(cur), len(NEXT))
            while j < length:
                if cur[j] != NEXT[j]:
                    # 建图
                    graph[ord(cur[j]) - ord('a')].append(ord(NEXT[j]) - ord('a'))
                    indegree[ord(NEXT[j]) - ord('a')] += 1
                    break
                j += 1
            if j < len(cur) and j == len(NEXT):
                return ""
        q = [0 for i in range(26)]
        l, r = 0, 0
        kinds = 0 # 字符出现的种类
        for  i in range(26):
            if indegree[i] != -1:
                kinds += 1
            if indegree[i] == 0:
                q[r] = i
                r += 1
        ret = []
        while l < r:
            cur = q[l]
            l += 1
            ret.append(chr(cur + ord('a')))
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q[r] = nei
                    r += 1
        return ''.join(ret) if len(ret) == kinds else ""