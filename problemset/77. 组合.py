import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def _combine(s, t):
            nonlocal ret
            if len(t) == k:
                t_c = copy.deepcopy(t)
                ret.append(t_c)
                return
            for i in range(s, n + 1):
                t.append(i)
                _combine(i + 1, t)
                t.pop()
        _combine(1, [])
        return ret
