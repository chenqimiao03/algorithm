import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # n = len(nums)
        # def _r(status, nums):
        #     nonlocal result
        #     if len(status) == n:
        #         result.append([status[i] for i in range(n)])
        #         return
        #     for i in range(len(nums)):
        #         status.append(nums[i])
        #         _r(status, nums[:i] + nums[i+1:])
        #         status.pop()
        # _r([], nums)
        # return result
        """
        时间复杂度：O(N!*N)
        """
        ret = []
        def _f(i):
            nonlocal ret
            if i == len(nums):
                n_c = copy.deepcopy(nums)
                ret.append(n_c)
            else:
                for j in range(i, len(nums)):
                    nums[i], nums[j] = nums[j], nums[i]
                    _f(i + 1)
                    nums[i], nums[j] = nums[j], nums[i]
        _f(0)
        return ret