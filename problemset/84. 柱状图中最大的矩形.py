class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        时间复杂度：O(N^2)
        空间复杂度：O(1)
        """
        maxArea = -1
        for i in range(len(heights)):
            minHeight = heights[i]
            for j in range(i, len(heights)):
                minHeight = min(heights[j], minHeight)
                maxArea = max(maxArea, minHeight * (j - i + 1))
        return maxArea

