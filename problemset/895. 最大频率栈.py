from collections import deque

class FreqStack:

    def __init__(self):
        self.words = {}
        self.maxFreq = 0
        self.values = {}

    def push(self, val: int) -> None:
        # 词频统计：如果没出现过就设置成 1，否则就设置成之前出现过的次数加 1
        self.words[val] = 1 if val not in self.words else self.words[val] + 1
        # 获取当前值出现的词频
        curValFreq = self.words.get(val)
        # 如果当前词频没有相应的队列，就新建
        # 也可以用双向链表
        if curValFreq not in self.values:
            self.values[curValFreq] = deque()
        # 将当前值添加到相应的词频队列中
        self.values[curValFreq].append(val)
        # 更新最大词频
        self.maxFreq = max(self.maxFreq, curValFreq)

    def pop(self) -> int:
        q = self.values.get(self.maxFreq)
        ans = q.pop()
        # 最大词频队列为空
        if len(q) == 0:
            # 删除最大词频队列
            self.values.pop(self.maxFreq)
            # 最大词频减 1
            self.maxFreq -= 1
        # 删除一个值也需要在词频统计表将该值的词频更新
        times = self.words.get(ans)
        if times == 1:
            self.words.pop(ans)
        else:
            self.words[ans] -= 1
        return ans




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()