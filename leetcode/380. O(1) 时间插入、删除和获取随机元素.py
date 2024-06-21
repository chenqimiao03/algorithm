import random

class RandomizedSet:
    """
    验证链接：https://leetcode.cn/problems/insert-delete-getrandom-o1/ 
    """

    def __init__(self):
        self.hashMap = {
            # value: index
        }
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.array.append(val)
        self.hashMap[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            i = self.hashMap.get(val)
            last = len(self.array) - 1
            # 将数组末尾的元素放到第 i 个位置
            self.array[i], self.array[last] = self.array[last], self.array[i]
            self.hashMap[self.array[i]] = i
            self.hashMap.pop(self.array[-1])
            self.array.pop()
            return True
        return False

    def getRandom(self) -> int:
        i = random.choice(range(len(self.array)))
        return self.array[i]




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()