class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def f(cur, nums):
            nonlocal ans
            if len(cur) == n:
                ans.append([cur[i] for i in range(n)])
                return
            for i in range(len(nums)):
                cur.append(nums[i])
                f(cur, nums[:i] + nums[i + 1:])
                cur.pop()
        f([], nums)
        return ans



