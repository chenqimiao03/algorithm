import random


class RandomizedCollection:

    def __init__(self):
        self.hashMap = {}
        self.array = []


    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            self.array.append(val)
            self.hashMap[val].add(len(self.array) - 1)
            return False
        self.array.append(val)
        self.hashMap[val] = {len(self.array) - 1}
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            # 如果当前删除元素和数组最后一个值一样，直接删除数组最后一个就可以
            if val == self.array[-1]:
                self.hashMap.get(self.array[-1]).remove(len(self.array) - 1)
                self.array.pop()
                # 如果要删除的在当前容器中只有一个，那个就将这个值从字典中删除
                if len(self.hashMap.get(val)) == 0:
                    self.hashMap.pop(val)
            else:
                # 从集合中随机选取一个
                i = self.hashMap.get(val).pop()
                # 交换两个元素的值
                last = len(self.array) - 1
                self.array[last], self.array[i] = self.array[i], self.array[last]
                # 从数组中删除
                self.array.pop()
                # 如果要删除的在当前容器中只有一个，那个就将这个值从字典中删除
                if len(self.hashMap.get(val)) == 0:
                    self.hashMap.pop(val)
                if len(self.array) != 0:
                    self.hashMap.get(self.array[i]).remove(last)
                    self.hashMap.get(self.array[i]).add(i)
            return True
        return False


    def getRandom(self) -> int:
        i = random.choice(range(len(self.array)))
        return self.array[i]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()