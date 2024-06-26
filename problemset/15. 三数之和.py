class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        时间复杂度：O(N^2)
        空间复杂度：O(1)
        """
        ret = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
        return ret