class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        import math
        def isPalindrome(num):
            """判断一个数是不是回文数
            """
            offset = 1
            while num // offset >= 10:
                offset *= 10
            while num != 0:
                if num // offset != num % 10:
                    return False
                num = (num % offset) // 10
                offset //= 100
            return True

        def odd(seed):
            ret = seed
            seed //= 10
            while seed != 0:
                ret = ret * 10 + (seed % 10)
                seed //= 10
            return ret

        def even(seed):
            ret = seed
            while seed != 0:
                ret = ret * 10 + (seed % 10)
                seed //= 10
            return ret
        
        def check(num, l, r):
            return num >= l and num <= r and isPalindrome(num)
        
        l, r = int(left), int(right)
        limit = int(math.sqrt(r))
        seed = 1
        num = 0
        ret = 0
        while True:
            # 生成偶数长度的回文数字
            # 123 -> 123321
            num = even(seed)
            if check(num * num, l, r):
                ret += 1
            # 生成奇数长度的回文数字
            # 123 -> 12321
            num = odd(seed)
            if check(num * num, l, r):
                ret += 1
            seed += 1
            if num >= limit:
                break
        return ret