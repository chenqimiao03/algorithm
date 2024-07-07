class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ret = 0
        for i in range(n):
            # 严格大压小
            while stack and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                left = stack[-1] if stack else -1
                ret = max(ret, (i - left - 1) * heights[top])
            stack.append(i)
        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1
            ret = max(ret, (n - left - 1) * heights[top])
        return ret

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """时间复杂度：O(N*M)
        """
        # 压缩 1
        n, m = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
        ret = 0
        for i in range(n):
            if i == 0:
                ret = max(ret, self.largestRectangleArea(matrix[0]))
            else:
                for j in range(m):
                    # 如果某列上的 1 连续
                    if matrix[i][j] != 0 and matrix[i - 1][j] != 0:
                        matrix[i][j] += matrix[i - 1][j]
                ret = max(ret, self.largestRectangleArea(matrix[i]))
        return ret