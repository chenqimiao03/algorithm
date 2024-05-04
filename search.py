def bsearch(arr: [], num: int) -> bool: # noqa
    """
    在有序数组中确定 num 存在还是不存在
    :param arr:
    :return:
    """
    if len(arr) == 0:
        return False
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return False


def bsearch_ext_1(arr: [], num: int) -> int:
    """
    在有序数组中找大于等于 num 的最左位置
    :param arr:
    :param num:
    :return:
    """
    if len(arr) == 0:
        return -1
    left, right, ret = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] >= num:
            right = mid - 1
            ret = mid
        else:
            left = mid + 1
    return ret


def bsearch_ext_2(arr: [], num: int) -> int:
    """
    在有序数组中找小于等于 num 的最右位置
    :param arr:
    :param num:
    :return:
    """
    if len(arr) == 0:
        return -1
    left, right, ret = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] <= num:
            ret = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret


def findPeakElement(arr: []):
    """
    寻找峰值
    题目出处：https://leetcode.cn/problems/find-peak-element/，其中对于任意 i，arr[i] != arr[i + 1]
    :param arr:
    :return:
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
