class Solution:
    def decodeString(self, s: str) -> str:
        def f(i):
            nonlocal where
            cur = 0
            path = []
            while i < n and s[i] != ']':
                if s[i] >= '0' and s[i] <= '9':
                    cur = cur * 10 + ord(s[i]) - ord('0')
                    i += 1
                elif s[i] != '[':
                    path.append(s[i])
                    i += 1
                else:
                    t = f(i + 1)
                    for i in range(cur):
                        path.append(t)
                    i = where + 1
                    cur = 0
            where = i
            return "".join(path)
        where, n = 0, len(s)
        return f(0)