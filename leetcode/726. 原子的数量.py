class Solution:
    def countOfAtoms(self, s: str) -> str:
        def fill(ret, name, pre, cnt):
            if len(name) > 0 or pre:
                cnt = 1 if cnt == 0 else cnt
                if len(name):
                    key = ''.join(name)
                    ret[key] = ret.get(key, 0) + cnt
                else:
                    for key in pre.keys():
                        ret[key] = ret.get(key, 0) + pre.get(key) * cnt
            
        def f(i):
            nonlocal where
            cnt = 0
            ret, pre = {}, {}
            name = []
            while i < n and s[i] != ')':
                if (s[i] >= 'A' and s[i] <= 'Z') or s[i] == '(':
                    fill(ret, name, pre, cnt)
                    name.clear()
                    pre.clear()
                    cnt = 0
                    if s[i] >= 'A' and s[i] <= 'Z':
                        name.append(s[i])
                        i += 1
                    else:
                        pre = f(i + 1)
                        i = where + 1
                elif s[i] >= 'a' and s[i] <= 'z':
                    name.append(s[i])
                    i += 1
                else:
                    cnt = cnt * 10 + (ord(s[i]) - ord('0'))
                    i += 1
            fill(ret, name, pre, cnt)
            where = i
            return ret
        n, where = len(s), 0
        ret = []
        items = sorted(f(0).items(), key=lambda x: x[0])
        for item in items:
            ret.append(item[0])
            if item[1] != 1:
                ret.append(str(item[1]))
        return ''.join(ret)

