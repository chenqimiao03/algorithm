class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 对于每个位置 arr[i] 都求左右两边最小值的位置 (j, k)
        MOD = 10 ** 9 + 7
        n = len(arr)
        stack = []
        r = 0
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                left = stack[-1] if stack else -1
                r = (r + (top - left) * (i - top) * arr[top]) % MOD
            stack.append(i)
        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1
            r = (r + (top - left) * (n - top) * arr[top]) % MOD
        return r