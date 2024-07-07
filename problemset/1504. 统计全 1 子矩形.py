class Solution:
    def count(self, arr):
        # 统计以 [a, b, c, d,..., k] 为底的矩形有多少个
        m = len(arr)
        stack = [] # 大压小
        ret = 0
        # 当栈非空并且栈顶元素的值大于等于当前值（栈无法保持单调性）
        for i in range(m):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                if arr[top] > arr[i]:
                    left = stack[-1] if stack else -1 # 左边界
                    width = i - left - 1 # 宽度
                    height = 0 if left == -1 else arr[left]
                    height = max(height, arr[i])
                    # arr[top], arr[top-1],..., height+1
                    ret += (arr[top] - height) * width * (width + 1) // 2
            stack.append(i)
        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1 # 左边界
            width = m - left - 1 # 宽度
            # 求边界两点的最大值
            height = 0 if left == -1 else arr[left]
            # 求 arr[top], arr[top-1],..., height+1
            ret += (arr[top] - height) * width * (width + 1) // 2
        return ret

    def numSubmat(self, mat: List[List[int]]) -> int:
        ret = 0
        n, m = len(mat), len(mat[0])
        for i in range(n):
            if i != 0:
                for j in range(m):
                    if mat[i][j] != 0 and mat[i - 1][j] != 0:
                        mat[i][j] += mat[i - 1][j]
            ret += self.count(mat[i])
        return ret