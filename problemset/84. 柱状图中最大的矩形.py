class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        时间复杂度：O(N^2)
        空间复杂度：O(1)
        """
        # maxArea = -1
        # for i in range(len(heights)):
        #     minHeight = heights[i]
        #     for j in range(i, len(heights)):
        #         minHeight = min(heights[j], minHeight)
        #         maxArea = max(maxArea, minHeight * (j - i + 1))
        # return maxArea
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