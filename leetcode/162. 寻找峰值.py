class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        """其中对于任意 i，arr[i] != arr[i + 1]
        """
        n = len(arr)
        if n == 1:
            return 0
        # 单独验证 0 位置是不是峰值点
        if arr[0] > arr[1]:
            return 0
        # 单独验证 n - 1 位置是不是峰值点
        if arr[n - 2] < arr[n - 1]:
            return n - 1
        # 由于左边是上升趋势，右边是下降趋势，联想零点定理可知：中间必定存在峰值
        left, right, ret = 1, n - 2, -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            # 中间点左侧是下降趋势
            if arr[mid - 1] > arr[mid]:
                right = mid - 1
            # 中间点右侧是上升趋势
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                ret = mid
                break
        return ret