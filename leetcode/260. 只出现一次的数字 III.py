class Solution:
    """
    验证链接：https://leetcode.cn/problems/single-number-iii/
    由于恰好有两个元素（x, y）只出现一次，其余所有元素均出现两次，故 eor1 的结果是 x ^ y
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        eor1 = 0
        for num in nums:
            eor1 ^= num
        # brain kernighan 算法
        # 提取出二进制里最右侧的 1
        right = eor1 & (-eor1)
        eor2 = 0
        for num in nums:
            # 将原数组中所有的数分为两类：一类是在 right 位为 1 的数和在 right 位不为 1 的数
            if (num & right) == 0:
                eor2 ^= num
        return [eor2, eor1 ^ eor2]
