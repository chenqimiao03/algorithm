import random
from typing import List

class Solution:
    def randomizedSelect(self, arr, i):
        """
        查找 arr 中下标为 i 的数是哪一个（利用随机快速排序分区的思路，一次将一批相同的数据放在中间位置，然后判断 i 是不是在中间位置）
        :param arr:
        :param i:
        :return:
        """
        def partition(l, r, x):
            nonlocal arr
            a, b, i = l, r, l
            while i <= b:
                if arr[i] == x:
                    i += 1
                elif arr[i] < x:
                    arr[i], arr[a] = arr[a], arr[i]
                    a += 1
                    i += 1
                else:
                    arr[i], arr[b] = arr[b], arr[i]
                    b -= 1
            return a, b
        ans, l, r = 0, 0, len(arr) - 1
        while l <= r:
            a, b = partition(l, r, arr[l + int(random.random() * (r - l + 1))])
            if i < a:
                r = a - 1
            elif i > b:
                l = b + 1
            else:
                ans = arr[i]
                break
        return ans

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.randomizedSelect(nums, len(nums) - k)
