class Solution:
    def calculate(self, s: str) -> int:
        def push(numbers, op, cur):
            if op == '+':
                numbers.append(cur)
            elif op == '-':
                numbers.append(-cur)
            elif op == '*':
                numbers.append(cur * numbers.pop())
            else:
                numbers.append(numbers.pop() // cur)
        def f(i):
            nonlocal where
            numbers = []
            op = '+'
            cur = 0
            while i < n and s[i] != ')':
                if s[i] >= '0' and s[i] <= '9':
                    cur = cur * 10 + ord(s[i]) - ord('0')
                    i += 1
                elif s[i] == ' ':
                    i += 1
                    continue
                elif s[i] != '(':
                    # +, -, *, //
                    push(numbers, op, cur)
                    cur = 0
                    op = s[i]
                    i += 1
                else:
                    cur = f(i + 1)
                    i = where + 1
            if cur:
                push(numbers, op, cur)
            where = i
            return sum(numbers)
        n, where = len(s), 0
        return f(0)
