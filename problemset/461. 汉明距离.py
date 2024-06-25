class Solution:
    """
    验证链接：https://leetcode.cn/problems/hamming-distance/
    """
    def hammingDistance(self, x: int, y: int) -> int:
        def cntOnes(n):
            """
            统计二进制1的个数
            :param n:
            :return:
            """
            # cnt = 0
            # for i in range(32):
            #     cnt += (n >> i) & 1
            # return cnt
            # 将二进制每一个位看成一个长度
            n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
            n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
            n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
            n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
            n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
            return n
        return cntOnes(x ^ y)
