class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        ret = 2 ** 31 - 1
        for r in range(len(nums)):
            total += nums[r]
            # l 位置上的数能不能从这个窗口中出去
            while total - nums[l] >= target:
                total -= nums[l]
                l += 1
            if total >= target:
                ret = min(ret, r - l + 1)
        return 0 if ret == 2 ** 31 - 1 else ret