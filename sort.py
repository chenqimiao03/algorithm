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
        a = [random.choice(range(1, 10000)) for _ in range(100)]
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
        "insertionSort": insertionSort
    }
    test(functions, "selectionSort")
    test(functions, "bubbleSort")
    test(functions, "insertionSort")
