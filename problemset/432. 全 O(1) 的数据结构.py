import random


class ListNode:

    def __init__(self, cnt, next=None, prev=None):
        self.cnt = cnt
        self.hashSet = set()
        self.next = next
        self.prev = prev


class AllOne:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.words = {}  # {str: addr}

    @staticmethod
    def insert(cur: ListNode, pos: ListNode):
        cur.next.prev = pos
        pos.next = cur.next
        cur.next = pos
        pos.prev = cur

    @staticmethod
    def remove(cur: ListNode):
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def inc(self, key: str) -> None:
        # 如果该字符串没有出现过
        if key not in self.words:
            # 如果头节点的下一个节点的词频值就是1，直接添加在词频为1的桶里
            if self.head.next.cnt == 1:
                self.words[key] = self.head.next
                self.head.next.hashSet.add(key)
            else:
                n = ListNode(1)
                n.hashSet.add(key)
                self.words[key] = n
                # 在双向链表的头节点之后插入一个新节点
                self.insert(self.head, n)
        else:
            n = self.words.get(key)
            if n.next.cnt == n.cnt + 1:
                self.words[key] = n.next
                n.next.hashSet.add(key)
            else:
                nn = ListNode(n.cnt + 1)
                nn.hashSet.add(key)
                self.words[key] = nn
                self.insert(n, nn)
            n.hashSet.remove(key)
            if len(n.hashSet) == 0:
                self.remove(n)

    def dec(self, key: str) -> None:
        if key in self.words:
            n = self.words.get(key)
            if n.cnt == 1:
                self.words.pop(key)
            else:
                if n.prev.cnt == n.cnt - 1:
                    self.words[key] = n.prev
                    n.prev.hashSet.add(key)
                else:
                    nn = ListNode(n.cnt - 1)
                    nn.hashSet.add(key)
                    self.words[key] = nn
                    self.insert(n.prev, nn)
            n.hashSet.remove(key)
            if len(n.hashSet) == 0:
                self.remove(n)

    def getMaxKey(self) -> str:
        return "" if len(self.tail.prev.hashSet) == 0 else random.choice(list(self.tail.prev.hashSet))

    def getMinKey(self) -> str:
        return "" if len(self.head.next.hashSet) == 0 else random.choice(list(self.head.next.hashSet))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()