class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ret = [0 for i in range(n)]
        for i in range(n):
            # 严格小于的：单调栈（大压小）
            # 严格大于的：单调栈（小压大）
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                ret[top] = i - top
            # 相等也能进栈
            stack.append(i)
        # 由于之后不出现比当前的气温高的，可以用 0 代替
        return ret
