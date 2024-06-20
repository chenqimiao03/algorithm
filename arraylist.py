from array import array
import random


class ArrayList:

    def __init__(self, n):
        # datatype: https://docs.python.org/zh-cn/3.8//library/array.html#module-array
        self._data = array('i', [0 for i in range(n)])
        self._cap = n
        self._size = 0
    
    def __getitem__(self, idx):
        if idx < 0 or idx > self._size:
            raise IndexError(f'idx must be ge 0 and le {self._size}')
        return self._data[idx]

    def __setitem__(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f'idx must be ge 0 and le {self._size}')
        self._data[idx] = value

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]
    
    def ensureCapacityInternal(self):
        if self._size >= self._cap:
            self._cap *= 2
            data = array('i', [0 for i in range(self._cap)])
            for i in range(self._size):
                data[i] = self._data[i]
            self._data = data
    
    def append(self, val):
        """
        时间复杂度：O(1)
        """
        self.ensureCapacityInternal()
        self._data[self._size] = val
        self._size += 1


    def insert(self, val, idx):
        """
        时间复杂度：O(N)
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f'idx must be ge 0 and le {self._size}')
        self.ensureCapacityInternal()
        for i in range(self._size - 1, idx - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[idx] = val
        self._size += 1

    def pop(self, idx):
        """
        时间复杂度：O(N)
        """
        if self._size == 0:
            raise IndexError('pop from empty list')
        if idx < 0 or idx > self._size:
            raise IndexError(f'idx must be ge 0 and le {self._size}')
        for i in range(idx, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
    
    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    n = 1000
    testTimes = 1000000
    array1 = ArrayList(n)
    array2 = list()
    print("测试开始")
    print("调用阶段开始")
    for i in range(testTimes):
        decide = random.random()
        number = int(random.random() * n)
        if decide < 0.333:
            # append
            array1.append(number)
            array2.append(number)
        elif decide < 0.666:
            # pop
            if len(array1) == 0:
                continue
            idx = random.choice(range(len(array1)))
            array1.pop(idx)
            array2.pop(idx)
        else:
            # insert index
            if len(array1) == 0:
                idx = 0
            else:
                idx = random.choice(range(len(array1)))
            array1.insert(number, idx)
            array2.insert(idx, number)
    print("调用阶段结束")
    print("验证阶段开始")
    if len(array1) != len(array2):
        print('出错了')
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            print("出错了！")
    print("验证阶段结束")
    print("测试结束")
