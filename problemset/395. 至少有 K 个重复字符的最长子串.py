class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        cnts = [0 for i in range(26)]
        ret = 0
        # 枚举：req 种字符都要大于等于 k 的字符串
        for req in range(1, 27):
            for i in range(26):
                cnts[i] = 0
            l = 0
            # 字符的种类
            c = 0
            # 满足大于等于 k 次的字符种类
            sat = 0
            for r in range(n):
                j = ord(s[r]) - ord('a')
                # 词频统计
                cnts[j] += 1
                if cnts[j] == 1:
                    c += 1
                if cnts[j] == k:
                    sat += 1
                # [l ... r] 这个窗口中统计到的字符种类超过了当前所需要的 req
                # l 位置从窗口吐出
                while c > req:
                    a = ord(s[l]) - ord('a')
                    if cnts[a] == 1:
                        c -= 1
                    if cnts[a] == k:
                        sat -= 1
                    cnts[a] -= 1
                    l += 1
                if sat == req:
                    ret = max(ret, r - l + 1)
        return ret

