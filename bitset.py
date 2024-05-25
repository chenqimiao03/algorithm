import random


class BITSet:
    """
    位图其实就是用一段连续的比特【比特组成的数组】中的第N个比特来表示无符号整数N，用比特状态1和0表示该数存不存在，取值和存值操作都用位运算
    优点：节省内存空间，因为一个数字只占用1个比特的空间
    """
    def __init__(self, n):
        self.n = n
        # a / b 的结果向上取整也可以写成 (a + b - 1) / b
        # 前提 a 和 b 都是非负数
        self.array = bytearray((n // 8) + 1)

    def add(self, num):
        """
        把 num 加入到位图
        :param num:
        :return:
        """
        i, j = num // 8, num % 8
        self.array[i] |= (1 << j)

    def remove(self, num):
        """
        把 num 从位图中删除
        :param num:
        :return:
        """
        i, j = num // 8, num % 8
        self.array[i] &= ~(1 << j)

    def reverse(self, num):
        """
        如果位图中没有 num 就加入；如果位图里有 num 就删除。
        :param num:
        :return:
        """
        # if num in self:
        #     self.remove(num)
        # else:
        #     self.add(num)
        i, j = num // 8, num % 8
        self.array[i] ^= (1 << j)

    def __contains__(self, item):
        """
        查询 item 是否在位图中
        :param item:
        :return:
        """
        i, j = item // 8, item % 8
        return self.array[i] & (1 << j)


if __name__ == '__main__':
    n = 1000
    testTimes = 10000
    bitset = BITSet(n)
    hashSet = set()
    print("测试开始")
    print("调用阶段开始")
    for i in range(testTimes):
        decide = random.random()
        number = int(random.random() * n)
        if decide < 0.333:
            bitset.add(number)
            hashSet.add(number)
        elif decide < 0.666:
            bitset.remove(number)
            if number in hashSet:
                hashSet.remove(number)
        else:
            bitset.reverse(number)
            if number in hashSet:
                hashSet.remove(number)
            else:
                hashSet.add(number)
    print("调用阶段结束")
    print("验证阶段开始")
    for i in range(n):
        if (i in bitset) != (i in hashSet):
            print("出错了！")
    print("验证阶段结束")
    print("测试结束")
