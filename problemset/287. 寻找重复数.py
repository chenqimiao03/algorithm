class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        # HashMap = {}
        # for i in range(len(nums)):
        #     if HashMap.get(nums[i], None) is None:
        #         HashMap[nums[i]] = 1
        #     else:
        #         return nums[i]
        # return -1
        
        # 有环的静态链表
        n = len(nums)
        if n < 2:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow