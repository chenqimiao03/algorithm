import random
import copy


def selectionSort(arr: []) -> None: # noqa
    """
    在 [i, n - 1] 的范围上，找到最小值并放在 i 的位置，然后在 [i + 1, n - 1] 上继续
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return None
    for i in range(len(arr) - 1):
        minIndex = i # noqa
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j # noqa
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return None


def bubbleSort(arr: []) -> None: # noqa
    """
    在 [0, i] 的范围上，相邻位置较大的数滚下去，最大值最终来到 i 的位置，然后在 [0, i - 1] 上继续
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return None
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return None


def insertionSort(arr: []) -> None: # noqa
    """
    在 [0, i] 的范围上已经有序，新来的数从右到左滑到不再比它小的位置上插入，然后继续
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return None
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return None


def mergeSoer(arr: []):
    """
    归并排序（非递归版本）
    验证链接：https://leetcode.cn/problems/sort-an-array/description/
    :param arr:
    :return:
    """
    n, step = len(arr), 1
    HELP = [None for _ in range(n)]

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

    while step < n:
        l = 0
        while l < n:
            mid = l + step - 1
            # 右边没有数据了
            if mid + 1 >= n:
                break
            # 一遍情况右边界的取值为：l + 2 * step - 1，但是当 l + 2 * step  - 1 大于 n - 1 时，右边界必定是 n - 1
            r = min(l + (step << 1) - 1, n - 1)
            _merge(l, mid, r)
            l = r + 1
        step <<= 1


def quickSort(arr):
    """
    随机快速排序

    :param arr:
    :return:
    """
    def partition(l, r, x):
        """
        将数组 arr 划分成两部分，其中左边的数都小于等于 x，右边的数都大于 x
        :param l:
        :param r:
        :param x:
        :return:
        """
        nonlocal arr
        a, xi = l, 0
        for i in range(l, r + 1):
            if arr[i] <= x:
                # swap arr[i], arr[a]
                arr[a], arr[i] = arr[i], arr[a]
                if arr[a] == x:
                    xi = a
                a += 1
        # 将小于等于 x 的这一部分的最后一个数改为 x
        arr[xi], arr[a - 1] = arr[a - 1], arr[xi]
        return a - 1
    def partition_1(l, r, x):
        """
        将数组 arr 划分成两部分，其中左边的数都小于等于 x，中间部分的数都等于 x，右边的数都大于 x（这种思想可以用于解决荷兰国旗问题）
        :param l:
        :param r:
        :param x:
        :return:
        """
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

    def _quickSort(l, r):
        nonlocal arr
        if l >= r:
            return
        # 随机选取 arr[l ... r] 中的一个数
        x = arr[l + int(random.random() * (r - l + 1))]
        # mid = partition(l, r, x)
        # _quickSort(l, mid - 1)
        # _quickSort(mid + 1, r)
        a, b = partition_1(l, r, x)
        _quickSort(l, a - 1)
        _quickSort(b + 1, r)
    _quickSort(0, len(arr) - 1)
    return arr


def heapSort(arr):
    """
    堆排序
    :param arr:
    :return:
    """
    def heapify(size):
        """
        从上往下调整大根堆
        :param:
        :return:
        """
        nonlocal arr
        # 左孩子的位置
        i = 0
        l = 2 * i + 1
        # 有左孩子
        while l < size:
            # 取左右孩子最大值的下标
            best = l + 1 if l + 1 < size and arr[l + 1] > arr[l] else l
            best = best if arr[best] > arr[i] else i
            if best == i:
                break
            arr[best], arr[i] = arr[i], arr[best]
            i = best
            l = i * 2 + 1

    for i in range(len(arr)):
        # 建堆
        while i > 0 and arr[i] > arr[(i - 1) // 2]:
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = (i - 1) // 2
    size = len(arr)
    while size > 1:
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
        heapify(size)
    return arr


def countSort(arr):
    """
    计数排序
    :param arr:
    :return:
    """
    n = len(arr)
    minValue = min(arr)
    # 对数组中每一个数字，减去数组中的最小值，就可以把 arr 转成了非负数组
    for i in range(n):
        arr[i] -= minValue
    maxValue = max(arr)
    count = [0 for _ in range(maxValue + 1)]
    # 统计每个数出现的次数
    for i in range(n):
        count[arr[i]] += 1
    k = 0
    for i in range(maxValue + 1):
        for j in range(count[i]):
            arr[k] = i
            k += 1
    for i in range(n):
        arr[i] += minValue
    return arr


def radixSort(arr):
    """
    基数排序
    :param arr:
    :return:
    """
    def _radixSort(m):
        """
        基数排序核心代码
        :param m: arr 中最大值在 BASE 进制下有几位
        :return:
        """
        offset = 1
        nonlocal BASE, arr, CNTS, HELP
        n = len(arr)
        while m > 0:
            CNTS = [0 for _ in range(len(CNTS))]
            for i in range(n):
                # 提取 arr[i] 的第 offset 位的数字
                CNTS[(arr[i] // offset) % BASE] += 1
            # 处理成前缀次数累加的形式
            for i in range(1, BASE):
                CNTS[i] = CNTS[i] + CNTS[i - 1]
            # 从右往左遍历是为了保持原有的相对顺序
            for i in range(n - 1, -1, -1):
                j = (arr[i] // offset) % BASE
                CNTS[j] -= 1
                HELP[CNTS[j]] = arr[i]
            for i in range(n):
                arr[i] = HELP[i]
            m -= 1
            offset *= BASE

    def _numbt(number): # number of bit
        """
        获取数组中最大的数有多少位
        :return:
        """
        ans = 0
        while number > 0:
            ans += 1
            number //= BASE
        return ans

    n = len(arr)
    HELP = [None for i in range(n)]
    BASE = 10
    CNTS = [None for i in range(BASE)]
    if n > 1:
        # 获取数组中的最小值
        minValue = min(arr)
        # 对数组中每一个数字，减去数组中的最小值，就可以把 arr 转成了非负数组
        for i in range(n):
            arr[i] -= minValue
        maxValue = max(arr)
        _radixSort(_numbt(maxValue))
        # 还原数组中原来的数据
        for i in range(n):
            arr[i] += minValue
    return arr


def test(functions: dict, name: str) -> None: # noqa
    """
    对数器
    1. 你想要测的方法 A
    2. 实现复杂度不好但是容易实现的方法 B【往往是暴力解】
    3. 实现一个随机样本产生器【长度和值都是随机的】
    4. 把方法 A 和方法 B 跑相同的输入样本，看看得到的结果是否一样
    5. 如果有一个随机样本使得对比结果不一致，打印这个出错样本，并使用这个出错样本对方法 A 和方法 B 进行调试
    6. 当很多样本在这两个方法的对比下依然正确，可以确定方法 A 已经正确
    :param functions:
    :param name:
    :return:
    """
    results = []
    for _ in range(100):
        a = [random.choice(range(1, 100)) for _ in range(100)]
        b = copy.deepcopy(a)
        b.sort()
        functions[name](a)
        results.append(all(map(lambda x: x[0] == x[1], zip(a, b))))
    print(all(results))
    return None


if __name__ == '__main__':
    functions = {
        "selectionSort": selectionSort,
        "bubbleSort": bubbleSort,
        "insertionSort": insertionSort,
        "quickSort": quickSort,
        "heapSort": heapSort,
        "countSort": countSort,
        "radixSort": radixSort
    }
    # test(functions, "selectionSort")
    # test(functions, "bubbleSort")
    # test(functions, "insertionSort")
    # test(functions, "quickSort")
    # test(functions, "heapSort")
    # test(functions, "countSort")
    test(functions, "radixSort")

