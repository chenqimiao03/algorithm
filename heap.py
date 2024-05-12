"""
堆结构：是一种特殊的完全二叉树

完全二叉树和数组前缀范围的对应：
1. i 位置的父亲节点是：(i - 1) / 2
2. i 位置的左孩子是：(i * 2) + 1
3. i 位置的右孩子是：(i * 2) + 2

堆的定义（大顶堆）：这个结构中任何一个子结构的最大值都在其顶部
"""


class Heap:

    def __init__(self, n):
        self.cap = n
        self._data = [None for _ in range(n)]
        # 当前堆的大小
        self._size = 0

    def heappush(self, value):
        """
        从下往上调整大根堆
        :param value:
        :return:
        """
        if self._size >= self.cap:
            return
        self._data[self._size], i = value, self._size
        self._size += 1
        # 当前节点的值是否大于其父亲节点的值
        while i > 0 and self._data[i] > self._data[(i - 1) // 2]:
            self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
            i = (i - 1) // 2

    def heapify(self, i):
        """
        从 i 位置往下调整大根堆
        :param i:
        :return:
        """
        # 左孩子的位置
        l = 2 * i + 1
        # 有左孩子
        while l < self._size:
            # 取左右孩子最大值的下标
            best = l + 1 if l + 1 < self._size and self._data[l + 1] > self._data[l] else l
            # 当前节点与左右孩子的最大值作比较，然后取其最大值的下标
            best = best if self._data[best] > self._data[i] else i
            # 如果当前节点比其左右孩子的值都要大，那么符合堆的定义，无需继续往下调整
            if best == i:
                break
            # 当前节点与左右孩子的最大值交换位置，然后继续往下调整
            self._data[best], self._data[i] = self._data[i], self._data[best]
            i = best
            l = i * 2 + 1

    def heappop(self):
        if self._size:
            ret = self._data[0]
            self._data[0], self._data[self._size - 1] = self._data[self._size - 1], self._data[0]
            self._size -= 1
            self.heapify(0)
            return ret
        raise Exception('the heap is empty')
