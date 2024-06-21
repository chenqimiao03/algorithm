# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        while i > 0 and self._data[i].val < self._data[(i - 1) // 2].val:
            self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
            i = (i - 1) // 2

    def heapify(self, i):
        l = 2 * i + 1
        while l < self._size:
            best = l + 1 if l + 1 < self._size and self._data[l + 1].val < self._data[l].val else l
            best = best if self._data[best].val < self._data[i].val else i
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


class Solution:
    """
    验证链接：https://leetcode.cn/problems/vvXgSW/description/
    时间复杂度：
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        heap = Heap(k)
        for h in lists:
            # 如果当前头节点非空，就将当前头节点放到小顶堆中
            if h:
                heap.heappush(h)
        if heap.empty():
            return None
        head = ListNode(None)
        last = head
        while not heap.empty():
            cur = heap.heappop()
            last.next = cur
            if cur.next:
                heap.heappush(cur.next)
            # 尾指针向后移动
            last = cur
        return head.next