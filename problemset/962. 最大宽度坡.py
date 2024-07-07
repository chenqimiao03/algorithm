class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        ret = 0
        # 小压大
        for i in range(n):
            if len(stack) == 0 or nums[stack[-1]] > nums[i]: 
                stack.append(i)
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ret = max(ret, i - stack.pop())
        return ret