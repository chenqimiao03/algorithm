class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        i, j = 0, len(s) - 1
        s1 = s.lower()
        while i < j:
            # 如果不是数字和字母，就跳过该字符
            while i < j and (not (s1[i] in string.digits or s1[i] in string.ascii_lowercase)):
                i += 1
            while j > i and (not (s1[j] in string.digits or s1[j] in string.ascii_lowercase)):
                j -= 1
            # 如果两个字符不相等，该字符串不是回文串
            if s1[i] != s1[j]:
                return False
            i += 1
            j -= 1
        return True