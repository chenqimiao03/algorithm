class Heap:

    def __init__(self, n, cmp=lambda a, b: a > b):
        """大顶堆定义：maxHeap = Heap(n, cmp=lambda a, b: a > b)
        小顶堆定义：minHeap = Heap(n, cmp=lambda a, b: a < b)
        """
        self._cap = n
        self._data = [None for _ in range(n)]
        # 当前堆的大小
        self._size = 0
        self._cmp = cmp

    def heappush(self, value):
        """
        从下往上调整大根堆
        :param value:
        :return:
        """
        if self._size >= self._cap:
            return
        self._data[self._size], i = value, self._size
        self._size += 1
        # 当前节点的值是否大于/小于其父亲节点的值
        while i > 0 and self._cmp(self._data[i], self._data[(i - 1) // 2]):
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
            # 取左右孩子最大值/最小值的下标
            best = l + 1 if l + 1 < self._size and self._cmp(self._data[l + 1], self._data[l]) else l
            # 当前节点与左右孩子的最大值/最小值作比较，然后取其最大值/最小值的下标
            best = best if self._cmp(self._data[best], self._data[i]) else i
            # 如果当前节点比其左右孩子的值都要大/小，那么符合堆的定义，无需继续往下调整
            if best == i:
                break
            # 当前节点与左右孩子的最大值/最小值交换位置，然后继续往下调整
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
