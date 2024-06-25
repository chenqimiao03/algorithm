#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串一维数组
#
class Solution:
    def generatePermutation(self , s: str) -> List[str]:
        # write code here
        # 当输入的字符串为 "aab" 时，可以使用 hashmap 去重
        """
        时间复杂度：O(N*2^N)
        """
        ans = set()
        def _f(path, i):
            nonlocal ans
            if i == len(s):
                ans.add("".join(path))
                return
            # 要当前的字符
            path.append(s[i])
            _f(path, i + 1)
            # 不要当前字符
            path.pop()
            _f(path, i + 1)
        _f([], 0)
        ans = list(ans)
        ans.sort()
        return ans

