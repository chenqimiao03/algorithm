class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            ret = digits[i] + carry
            if ret >= 10:
                digits[i] = ret % 10
                carry = ret // 10
            else:
                digits[i] = ret
                carry = 0
        if carry:
            digits.insert(0, carry)
        return digits