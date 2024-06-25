class Solution:
    def isValid(self, s: str) -> bool:
        HASHMAP = {')': '(', ']': '[', '}': '{'}
        HASHSET = set('{([')
        stack = []
        for c in s:
            if c in HASHSET:
                stack.append(c)
            else:
                if len(stack) == 0 or HASHMAP.get(c) != stack[-1]:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
