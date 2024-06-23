class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        时间复杂度：O(N*2^N)
        """
        def f(nums, i, path, size, ans):
            if i == len(nums):
                cur = []
                for j in range(size):
                    cur.append(path[j])
                ans.append(cur)
            else:
                # 下一个的第一个数
                j = i + 1
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                # 不要当前相同数据
                f(nums, j, path, size, ans)
                # 要 k 个相同的数据
                for k in range(i, j):
                    path[size] = nums[k]
                    size += 1
                    f(nums, j, path, size, ans)
        nums.sort()
        ans = []
        f(nums, 0, [None for i in range(len(nums))], 0, ans)
        return ans
