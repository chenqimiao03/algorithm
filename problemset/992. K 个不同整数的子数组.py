class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def numsOfMostKinds(arr, k):
            nonlocal cnts
            for i in range(1, len(arr) + 1):
                cnts[i] = 0
            ret = 0
            l = 0
            # 字符的种类
            c = 0
            for r in range(len(arr)):
                cnts[arr[r]] += 1
                # 如果该字符在这个窗口中只出现了一次
                if cnts[arr[r]] == 1:
                    c += 1
                while c > k:
                    cnts[arr[l]] -= 1
                    if cnts[arr[l]] == 0:
                        c -= 1
                    l += 1
                ret += r - l + 1
            return ret
        cnts = [0 for i in range(200001)]
        return numsOfMostKinds(nums, k) - numsOfMostKinds(nums, k - 1)