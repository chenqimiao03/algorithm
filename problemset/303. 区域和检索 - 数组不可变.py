class NumArray:

    def __init__(self, nums: List[int]):
        self.cusum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.cusum[i + 1] = self.cusum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.cusum[right + 1] - self.cusum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)