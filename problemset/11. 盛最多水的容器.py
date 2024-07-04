class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. 暴力法
        时间复杂度：O(N^2)
        空间复杂度：O(1)
        """
        # ret = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         ret = max(ret, (j - i) * min(height[i], height[j]))
        # return ret
        """
        2. 双指针
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        # 谁小先结算谁
        i, j = 0, len(height) - 1
        ret = 0
        while i < j:
            minHeight = min(height[i], height[j])
            if minHeight == height[j]:
                j -= 1
            else:
                i += 1
            ret = max(ret, minHeight * (j - i + 1))
        return ret