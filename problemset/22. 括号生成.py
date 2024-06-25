class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def _generateParenthesis(s, left, right):
            nonlocal ret
            # 左右括号的数量都用完了
            if left == 0 and right == 0:
                # 也可以在生成的结果中过滤掉不符合要求的结果
                ret.append(s)
                return 
            # 添加右括号：只有右括号的数量多于左括号的数量时才能添加
            if right and right > left:
                _generateParenthesis(s + ")", left, right - 1)
            # 还有左括号的话就添加进去
            if left:
                _generateParenthesis(s + "(", left - 1, right)
        _generateParenthesis("", n, n)
        return ret
