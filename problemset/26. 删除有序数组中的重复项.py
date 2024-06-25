class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        while i < n:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
        return j