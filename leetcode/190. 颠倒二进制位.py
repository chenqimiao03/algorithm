class Solution:
    def reverseBits(self, n: int) -> int:
        # ans = 0
        # for i in range(32):
        #     ans |= ((n >> ((31 - i))) & 1) << i
        # return ans
        # 比如8位数 abcdefgh，颠倒后的结果位：hgfedcba
        # 先两两交换 1 位，badcfehg，那么可以 ((abcdefgh & 10101010) >> 1) | ((abcdefgh & 01010101) << 1)，即可得到
        # 由于数据范围是 32 位的，所以 1, 2, 4, 8, 16 依次交换
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n >> 16) | (n << 16)) & 0xffffffff
        return n
