class Solution:
    def balancedString(self, s: str) -> int:
        def ok(cnts, length, req):
            for i in range(4):
                # 某个字符在区间外的词频信息还大于 n // 4
                if cnts[i] > req:
                    return False
                # 当前字符还缺少几个才能达到 req
                length -= (req - cnts[i])
            # length 必须和每个字符需要修改的长度和一致
            return length == 0
    
        # 将 Q, W, E, R 分别转为 0, 1, 2, 3 方便做词频统计
        n = len(s)
        arr = [0 for i in range(n)]
        cnts = [0 for i in range(4)]
        for i in range(n):
            if s[i] == 'Q':
                arr[i] = 0
            elif s[i] == 'W':
                arr[i] = 1
            elif s[i] == 'E':
                arr[i] = 2
            else:
                arr[i] = 3
            cnts[arr[i]] += 1
        req = n // 4
        # 要修改几次才能做到四种字符一样多
        ret = n
        r = 0
        for l in range(n):
            # 窗口能否扩展
            while (not ok(cnts, r - l, req)) and (r < n):
                # 只统计窗口之外的词频信息
                cnts[arr[r]] -= 1
                r += 1
            if ok(cnts, r - l, req):
                ret = min(ret, r - l)
            cnts[arr[l]] += 1
        return ret