class Solution:
    """
    验证链接：https://leetcode.cn/problems/sort-an-array/
    """
    def sortArray(self, arr: List[int]) -> List[int]:
        HELP = [None for _ in range(len(arr))]
        def _merge(l, mid, r):
            nonlocal HELP
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

        def _mergeSort(l, r):
            if l == r:
                return
            mid = l + ((r - l) >> 1)
            _mergeSort(l, mid)
            _mergeSort(mid + 1, r)
            _merge(l, mid, r)
        _mergeSort(0, len(arr) - 1)
        return arr
