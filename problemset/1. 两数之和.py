class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        时间复杂度：O(N^2)
        空间复杂度：O(1)
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return i, j
        # return []
        """
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        HashMap = {}
        for i in range(len(nums)):
            if HashMap.get(target - nums[i]) == None:
                HashMap[nums[i]] = i
            else:
                return HashMap.get(target - nums[i]), i
        return -1, -1