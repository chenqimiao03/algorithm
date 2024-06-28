class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        HashMap = {0: 1} # 0 这个前缀和，在没有数字的时候已经有 1 次了
        ret, total = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            ret += HashMap.get(total - k, 0)
            HashMap[total] = 1 if HashMap.get(total, None) is None else HashMap[total] + 1
        return ret