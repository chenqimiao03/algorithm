class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ""
        cnts = [0 for i in range(256)]
        for c in t:
            cnts[ord(c)] -= 1
        # 最小覆盖子串的长度
        length = 2 ** 31 - 1
        # 这个最小覆盖子串是从哪里开始的
        start = 0
        l, r = 0, 0
        while r < n:
            # 当前字符在 t 字符串中有没有出现
            if cnts[ord(s[r])] < 0:
                m -= 1
            cnts[ord(s[r])] += 1
            # 当前区间已经包含了 t 字符串
            if m == 0:
                while cnts[ord(s[l])] > 0:
                    cnts[ord(s[l])] -= 1
                    l += 1
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l
            r += 1
        return "" if length == 2 ** 31 - 1 else ''.join(s[start: start + length])