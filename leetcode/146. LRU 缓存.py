class LRUCache:
    """
    最近最少使用缓存：双向链表+哈希表可以实现
    验证链接：https://leetcode.cn/problems/lru-cache/description/
    """

    class ListNode:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next, self.prev = None, None

    def __init__(self, capacity: int):
        self.head = type(self).ListNode(None, None)
        self.tail = type(self).ListNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.HashMap = {}

    def get(self, key: int) -> int:
        if self.HashMap.get(key) == None:
            return -1
        node = self.HashMap.get(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.HashMap.get(key) == None:
            if len(self.HashMap) >= self.capacity:
                # 最末尾的一个是最不常使用的
                last = self.tail.prev
                last.prev.next = last.next
                last.next.prev = last.prev
                self.HashMap.pop(last.key)
            node = type(self).ListNode(key, value)
            self.HashMap[key] = node
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
        else:
            node = self.HashMap.get(key)
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            node.value = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)