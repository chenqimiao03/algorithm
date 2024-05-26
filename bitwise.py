"""常见的位运算：
1. |：按位或
2. &：按位与
3. ^：按位异或
    异或运算的性质：
        （1）异或运算就是无进位相加
        （2）异或运算满足交换律、结合律，也就是说同一堆数字，不管异或顺序是什么，最终结果都是一个
        （3）0^n=n，n^n=0
        （4）整体异或和【一堆数字异或的最终结果】如果是x，整体中某部分异或和如果是y，那么剩下部分的异或和是x^y
    其中，第四点相关的题目最多，利用区间上异或和的性质
4. ~：按位取反
5. <<：左移，高位丢弃，低位补零
6. >>：右移，如果是非负数，低位丢弃，高位补零，如果是负数，低位丢弃，高位补 1
7. >>>：无符号右移

对于非负数，左移 i 位，相当于乘于 2 的 i 次方；右移 i 位，相当于除以 2 的 i 次方
"""
import random


def print_b(a):
    """
    打印 a 的二进制表示
    1. 负数在计算机中的表示：先看正数的二进制，减去 1，然后再按位取反
    2. 计算机中的二进制如何表示十进制：先取出符号位，然后按位取反，再加 1
    """
    for i in range(31, -1, -1):
        print("0" if a & (1 << i) == 0 else "1", end="")


def unm(a):
    """求 a 的相反数，除了整数最小值"""
    return ~a + 1


# 异或运算相关题目
# 1. 交换两个整数
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# 2. 在不使用比较操作的情况下获取两个数中的最大值
def MAX(a, b):
    def sign(n):
        """
        判断一个整数是不是无符号整数
        :param n:
        :return:
        """
        # 如果这个数是无符号数返回 1，否则返回 0
        return ((n >> 31) & 1) ^ 1
    c = a - b
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    # 判断 a 的符号和 b 的符号是否一样，如果不一样 diff 为 1，否则为 0
    diff = sa ^ sb
    # 判断 a 的符号和 b 的符号是否一样，如果不一样 same 为 0，否则为 1
    same = diff ^ 1
    # a 比 b 大的情况：
    # （1）a 和 b 符号不一样并且 a 是无符号整数
    # （2）a 和 b 符号一样并且 c 是无符号整数
    ra = diff * sa + same * sc
    rb = ra ^ 1
    return a * ra + b * rb


# 取一个数最右侧的 1
# brain kernighan 算法
def bk(n):
    return n & ((~n) + 1)


# 获取大于等于 n 的最小的 2 的幂次方
def near(n):
    if n <= 0:
        return 1
    n -= 1
    # 将最右的位都变成 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1


# 位运算实现加减乘除
# 加法：a ^ b + 进位信息（(a & b) << 1）
def add(a, b):
    def _add(a, b):
        ans = 0
        while b != 0:
            ans = (a ^ b) & 0xffffffff
            # 保存进位信息
            b = ((a & b) << 1) & 0xffffffff
            a = ans
        return ans
    ans = _add(a, b)
    return -_add(((~ans) & 0x7FFFFFFF), 1) if ans & 0x80000000 else ans


def neg(n):
    # 非 python 直接返回 ~a + 1
    if n > 0:
        return ~add(n, 0xffffffff)
    elif n == 0:
        return 0
    else:
        return add((~n & 0x7fffffff), 1)


def minus(a, b):
    # a - b = a + (-b) = a + (~b + 1)
    return add(a, neg(b))


def multipy(a, b):
    ans = 0
    x = neg(a) if a < 0 else a
    y = neg(b) if b < 0 else b
    while y != 0:
        if (y & 1) != 0:
            ans = add(ans, x)
        x <<= 1
        y >>= 1
    # 如果 a 和 b 同号，返回 x * y
    # 如果 a 和 b 不同号，返回 -(x * y)
    return ans if (a & 0x80000000) == (b & 0x80000000) else ~minus(ans, 1)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot equal 0")
    x = neg(a) if a < 0 else a
    y = neg(b) if b < 0 else b
    ans = 0
    for idx in range(30, -1, -1):
        if (x >> idx) >= y:
            ans |= 1 << idx
            x = minus(x, y << idx)
    return ans if (a & 0x80000000) == (b & 0x80000000) else ~minus(ans, 1)


if __name__ == '__main__':
    # print_b(4294967292)
    # a, b = 10, 20
    # print(MAX(a, b))
    # print(near(500))
    print(add(-1, -1))
