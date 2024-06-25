class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        时间复杂度：O(k*N)
        空间复杂度：O(1)
        """
        # n = len(nums)
        # k %= n
        # for i in range(k):
        #     last = nums[-1]
        #     for j in range(n - 1, 0, -1):
        #         nums[j] = nums[j - 1]
        #     nums[0] = last
        """
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        def reverse(start, end):
            nonlocal nums
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k , n - 1)