class Solution:
    def isPalindrome(self, num: int) -> bool:
        """判断一个数是不是回文数
        也可以转为字符串
        """
        if num < 0:
            return False
        offset = 1
        while num // offset >= 10:
            offset *= 10
        while num != 0:
            if num // offset != num % 10:
                return False
            num = (num % offset) // 10
            offset //= 100
        return True