class Heap:

    def __init__(self, n, compare):
        self.cap = n
        self._data = [None for _ in range(n)]
        # 当前堆的大小
        self._size = 0
        self.compare = compare

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
        # while i > 0 and self._data[i] > self._data[(i - 1) // 2]:
        while i > 0 and self.compare(self._data[i], self._data[(i - 1) // 2]):
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
            # 取左右孩子最值的下标
            # best = l + 1 if l + 1 < self._size and self._data[l + 1] > self._data[l] else l
            best = l + 1 if l + 1 < self._size and self.compare(self._data[l + 1], self._data[l]) else l
            # 当前节点与左右孩子的最值作比较，然后取其最值的下标
            # best = best if self._data[best] > self._data[i] else i
            best = best if self.compare(self._data[best], self._data[i]) else i
            # 如果当前节点比其左右孩子的值都要大或都要小，那么符合堆的定义，无需继续往下调整
            if best == i:
                break
            # 当前节点与左右孩子的最值交换位置，然后继续往下调整
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

    def size(self):
        return self._size

    def __getitem__(self, item):
        return self._data[item]


class MedianFinder:

    def __init__(self):
        self.maxHeap = Heap(100000, lambda a, b: a > b) # 流吐出较小的一半存放在大根堆中
        self.minHeap = Heap(100000, lambda a, b: a < b) # 流吐出较大的一半存放在小根堆中

    def addNum(self, num: int) -> None:
        # 如果大根堆和小根堆都是空，新来的数据放在大根堆中
        # 如果新来的数据小于等于大根堆堆顶，就放在大根堆中
        if self.maxHeap.size() == 0 or self.maxHeap[0] >= num:
            self.maxHeap.heappush(num)
        else:
            self.minHeap.heappush(num)
        self.balance()

    def balance(self):
        if abs(self.maxHeap.size() - self.minHeap.size()) == 2:
            if self.maxHeap.size() > self.minHeap.size():
                self.minHeap.heappush(self.maxHeap.heappop())
            else:
                self.maxHeap.heappush(self.minHeap.heappop())

    def findMedian(self) -> float:
        if self.maxHeap.size() == self.minHeap.size():
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        return self.maxHeap[0] if self.maxHeap.size() > self.minHeap.size() else self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()