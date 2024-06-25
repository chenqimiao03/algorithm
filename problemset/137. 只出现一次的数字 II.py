class Solution:
    """
    验证链接：https://leetcode.cn/problems/single-number-ii/
    """
    def find(self, nums, m):
        # 由于只有某个元素仅出现一次，其余每个元素都恰出现m次
        # 所以统计每位上1的个数，出现m次的元素在某个位上1的数量必定是m的整数倍
        cnts = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                cnts[i] += (num >> i) & 1
        ans = 0
        for i in range(30, -1, -1):
            if cnts[i] % m != 0:
                ans |= 1 << i
        # 如果是负数，那么先取出符号位，然后按位取反，再加 1
        return -(((~ans) & 0x7FFFFFFF) + 1) if cnts[31] % m else ans

    def singleNumber(self, nums: List[int]) -> int:
        """如果不要求使用常数级空间来解决，可以使用统计每个数出现的次数这种方法来解决
        """
        return self.find(nums, 3)
