class Solution:
    def trap(self, height: List[int]) -> int:
        # 在 i 位置能接到的雨水和 [0, i - 1]、[i + 1, n - 1] 的最大值相关
        # 从左到 i 的最大值可以用一个数组 left 记录
        # 从右到 i 的最大值可以用一个数组 right 记录
        # n = len(height)
        # left = [0 for i in range(n)]
        # right = [0 for i in range(n)]
        # for i in range(n):
        #     if i == 0:
        #         left[i] = height[i]
        #     else:
        #         left[i] = max(left[i - 1], height[i])
        # for i in range(n - 1, -1, -1):
        #     if i == n - 1:
        #         right[i] = height[i]
        #     else:
        #         right[i] = max(right[i + 1], height[i])
        # ret = 0
        # for i in range(1, n - 1):
        #     ret += max(0, min(left[i - 1], right[i + 1]) - height[i])
        # return ret
        l, r = 1, len(height) - 1
        lmax = height[0]
        rmax = height[len(height) - 1]
        ret = 0
        while l <= r:
            if lmax <= rmax:
                ret += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
                l += 1
            else:
                ret += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
                r -= 1
        return ret