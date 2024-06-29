class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # end = len(num) - 1
        # while end >= 0:
        #     if int(num[end]) != 0:
        #         break
        #     end -= 1
        # ret = []
        # for i in range(end + 1):
        #     ret.append(num[i])
        # return ''.join(ret)
        return num.rstrip('0')