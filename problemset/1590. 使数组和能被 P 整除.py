class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 整体余数
        mod = 0
        for num in nums:
            mod = (mod + num) % p
        # 整体余数是零，说明不需要移除子数组
        if mod == 0:
            return 0
        # key: 前缀和 % p 的余数
        # value: 最晚出现的位置
        HashMap = {0: -1}
        # 至少移除的长度
        ret = 2 ** 31 - 1
        current = 0
        for i in range(len(nums)):
            current = (current + nums[i]) % p
            find = (current - mod) if current >= mod else (current + p - mod)
            # find = (current + p - mod) % p
            if HashMap.get(find, None) is not None:
                ret = min(ret, i - HashMap.get(find))
            HashMap[current] = i
        return -1 if ret == len(nums) else ret