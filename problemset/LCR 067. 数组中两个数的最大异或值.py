class TrieTree:

    def __init__(self) -> None:
        self._N = 400001
        self._tree = [[0 for i in range(2)] for j in range(self._N)]
        self._cnt = 1
    
    def numberOfLeadingZeros(self, num):
        ret = 31
        for i in range(31, -1, -1):
            if num & (1 << i):
                ret = i
                break
        return ret
    
    def build(self, nums):
        self._cnt = 1
        maxValue = max(nums)
        self._left = self.numberOfLeadingZeros(maxValue)
        for num in nums:
            self.insert(num)

    def clear(self):
        for i in range(self._cnt):
            for j in range(2):
                self._tree[i][j] = 0
        self._cnt = 1
    
    def insert(self, num):
        cur = 1
        for i in range(self._left, -1, -1):
            j = (num >> i) & 1
            if self._tree[cur][j] == 0:
                self._cnt += 1
                self._tree[cur][j] = self._cnt
            cur = self._tree[cur][j]
    
    def maxXor(self, num):
        cur = 1
        ret = 0
        for i in range(self._left, -1, -1):
            j = (num >> i) & 1
            want = j ^ 1
            if self._tree[cur][want] == 0:
                want ^= 1
            ret |= (j ^ want) << i
            cur = self._tree[cur][want]
        return ret

# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         tree = TrieTree()
#         tree.build(nums)
#         ret = 0
#         for num in nums:
#             ret = max(ret, tree.maxXor(num))
#         tree.clear()
#         return ret

    def numberOfLeadingZeros(self, num):
        ret = 31
        for i in range(31, -1, -1):
            if num & (1 << i):
                ret = i
                break
        return ret
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxValue = max(nums)
        ret = 0
        s = set()
        # maxValue : 31 ... 28 全是 0
        # 从 27 位开始讨论
        # 讨论 27 位能不能达成 1
        # 讨论 26 位能不能达成 1
        # ...
        # 讨论 0 位能不能达成 1
        for i in range(self.numberOfLeadingZeros(maxValue), -1, -1):
            # ret: 31 ... i + 1 位已经达成目标
            # 讨论第 i 位能不能达成目标
            better = ret | (1 << i)
            s.clear()
            for num in nums:
                # 在 num 上保留 31 ... i 位的信息
                num = (num >> i) << i
                s.add(num)
                if (better ^ num) in s:
                    ret = better
                    break
        return ret