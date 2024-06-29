class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def move(c):
            if c == 'a':
                return 0
            elif c == 'e':
                return 1
            elif c == 'i':
                return 2
            elif c == 'o':
                return 3
            elif c == 'u':
                return 4
            else:
                return -1
    
        n = len(s)
        # 5 个元音字符，对应的状态只有 32 个不同的状态
        HashMap = [-2 for i in range(32)]
        HashMap[0], ret = -1, 0
        status = 0
        for i in range(n):
            # status：表示 0 ... i 位置上的字符串 aeiou 的奇偶性
            # 当前字符如果不是元音
            # 当前字符是元音 aeiou 修改相应的状态
            m = move(s[i])
            # 元音字符
            if m != -1:
                status ^= 1 << m
            # 同样的状态，之前出现在哪里
            if HashMap[status] != -2:
                ret = max(ret, i - HashMap[status])
            else:
                HashMap[status] = i
        return ret