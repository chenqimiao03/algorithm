class LFUCache:
    class LinkedList:

        class ListNode:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.freq = 1
                self.prev, self.next = None, None

        def __init__(self):
            self.head = type(self).ListNode(None, None)
            self.head.next = self.head
            self.head.prev = self.head
            self.size = 0

        def append(self, node: ListNode):
            # 尾插入, 加到双向链表尾部
            node.prev = self.head.prev
            node.next = self.head
            node.prev.next = node
            self.head.prev = node
            self.size += 1

        def pop(self, node: ListNode = None):
            if self.size == 0:
                return
            # 删除头部
            if node is None:
                node = self.head.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
            return node

    def __init__(self, capacity: int):
        from collections import defaultdict
        self.key_to_node = {}
        self.freq = defaultdict(type(self).LinkedList)
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node_freq = node.freq
        self.freq[node_freq].pop(node)
        # 如果当前节点的使用频率是最小的并且在该频率下的节点个数是 0
        # 那么最小频率应该随着该节点的访问频率增加而增加
        if self.min_freq == node_freq and self.freq[node_freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node_freq = node.freq
            self.freq[node_freq].pop(node)
            if self.min_freq == node_freq and self.freq[node_freq].size == 0:
                self.min_freq += 1
            node.freq += 1
            node.val = value
            self.freq[node.freq].append(node)
        else:
            if len(self.key_to_node) == self.capacity:
                node = self.freq[self.min_freq].pop()
                self.key_to_node.pop(node.key)
            node = type(self).LinkedList.ListNode(key, value)
            self.key_to_node[key] = node
            self.freq[1].append(node)
            self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)