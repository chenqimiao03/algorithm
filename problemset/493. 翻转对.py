from typing import List


class Solution:
    """
    验证链接：https://leetcode.cn/problems/reverse-pairs/
    """
    def reversePairs(self, arr: List[int]) -> int:
        HELP = [None for _ in range(len(arr))]
        def _merge(l, mid, r):
            nonlocal HELP
            ans, j = 0, mid + 1
            for i in range(l, mid + 1):
                while j <= r and arr[i] > arr[j] * 2:
                    j += 1
                ans += (j - mid - 1)
            i, a, b = l, l, mid + 1
            while a <= mid and b <= r:
                if arr[a] <= arr[b]:
                    HELP[i] = arr[a]
                    a += 1
                else:
                    HELP[i] = arr[b]
                    b += 1
                i += 1
            while a <= mid:
                HELP[i] = arr[a]
                a += 1
                i += 1
            while b <= r:
                HELP[i] = arr[b]
                b += 1
                i += 1
            for i in range(l, r + 1):
                arr[i] = HELP[i]
            return ans
    
        def solve(l, r):
            if l == r:
                return 0
            mid = l + ((r - l) >> 2)
            return solve(l, mid) + solve(mid + 1, r) + _merge(l, mid, r)

        return solve(0, len(arr) - 1)