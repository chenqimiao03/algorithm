class Heap:

    def __init__(self, n):
        self.cap = n
        self._data = [None for _ in range(n)]
        self._size = 0

    def heappush(self, value):
        if self._size >= self.cap:
            return
        self._data[self._size], i = value, self._size
        self._size += 1
        while i > 0 and self._data[i] < self._data[(i - 1) // 2]:
            self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
            i = (i - 1) // 2

    def heapify(self, i):
        l = 2 * i + 1
        while l < self._size:
            best = l + 1 if l + 1 < self._size and self._data[l + 1] < self._data[l] else l
            best = best if self._data[best] < self._data[i] else i
            if best == i:
                break
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

    def empty(self):
        return self._size == 0

    def __getitem__(self, item):
        return self._data[item]

    def size(self):
        return self._size


class Solution:
    """
    验证链接：https://leetcode.cn/problems/living-people-lcci/description/
    """
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        person = []
        for b, d in zip(birth, death):
            person.append((b, d))
        # 按照出生时间来排序
        person.sort(key=lambda x: x[0])
        if len(person) == 0:
            return 0
        # 未知数据规模，尽量给大点
        heap = Heap(1000001)
        heap.heappush(person[0][1])
        # 当前时间段存活最大人数
        maxPerson, ret = 1, person[0][0]
        for i in range(1, len(person)):
            # 弹出所有死亡时间小于当前出生时间的时间段
            while not heap.empty() and heap[0] < person[i][0]:
                heap.heappop()
            heap.heappush(person[i][1])
            # 获取当前时间有多少个人存活
            if maxPerson < heap.size():
                ret = person[i][0]
                maxPerson = heap.size()
        return ret

