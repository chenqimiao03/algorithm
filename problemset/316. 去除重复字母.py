class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnts = [0 for i in range(26)] # 每种字符的词频统计
        enter = [False for i in range(26)] # 判断每种字符有没有进栈
        for c in s:
            j = ord(c) - ord('a')
            cnts[j] += 1
        stack = [] # 大压小
        # 依次遍历字符串
        for c in s:
            # 将 a,b,c,...,z 映射到 0,1,2,...,25 上
            j = ord(c) - ord('a')
            # 如果当前字符没有在栈中
            if enter[j] is False:
                # 当前字符的 ascii 小于栈顶字符的 ascii，违反了字典序原则
                # 后续字符串中是否还有和当前字符相同的字符
                while stack and stack[-1] > c and cnts[ord(stack[-1]) - ord('a')] > 0:
                    enter[ord(stack[-1]) - ord('a')] = False
                    stack.pop()
                # 将当前字符放到栈中
                stack.append(c)
                enter[j] = True
            cnts[j] -= 1
        return ''.join(stack)