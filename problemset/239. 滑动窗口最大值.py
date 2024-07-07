class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque() # 大到小的队列
        # 先形成 k - 1 的窗口
        for i in range(k - 1):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        m = len(nums) - k + 1
        ret = [0 for i in range(m)]
        j = 0
        # 收集答案
        # 1. 将当前元素放到双端队列中
        # 2. 收集答案
        # 3. 把窗口的头弹出去（窗口最大值在窗口头）
        for i in range(k-1, len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # 双端队列的头部元素，总是窗口中的最大值
            ret[j] = nums[dq[0]]
            # 例如：[5, 4, 3, 2, 1], k=3
            if dq[0] == j:
                dq.popleft()
            j += 1
        return ret