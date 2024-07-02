class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 也可以用 ascii 映射成数组的下标来代替字典
        i, j, n, HashMap, result = 0, 0, len(s), {}, 0
        while j < n:
            if HashMap.get(s[j]) == None:
                HashMap[s[j]] = 1
            else:
                HashMap[s[j]] += 1
            # 寻找 s[j] 上一次出现的位置
            while HashMap[s[j]] > 1:
                HashMap[s[i]] -= 1
                i += 1
            result = max(result, (j - i + 1))
            j += 1
        return result
        # n, ret, l = len(s), 0, 0
        # HashMap = [0 for i in range(256)]
        # for r in range(n):
        #     j = ord(s[r])
        #     if HashMap[j] == 0:
        #         HashMap[j] = 1
        #     else:
        #         HashMap[j] += 1
        #     while HashMap[j] > 1:
        #         k = ord(s[l])
        #         HashMap[k] -= 1
        #         l += 1
        #     ret = max(ret, r - l + 1)
        # return ret

        # n = len(s)
        # 所有字符都没有上次出现的位置
        # last = [-1 for i in range(256)]
        # ret = 0
        # l = 0
        # for r in range(n):
        #     k = ord(s[r])
        #     l = max(l, last[k] + 1)
        #     ret = max(ret, r - l + 1)
        #     last[k] = r # 记录字符出现的位置
        #     r += 1
        # return ret