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
