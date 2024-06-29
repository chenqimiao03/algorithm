class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.matrix = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.matrix[i + 1][j + 1] = matrix[i][j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.matrix[i][j] += self.matrix[i][j - 1] + self.matrix[i - 1][j] - self.matrix[i - 1][j - 1]

    # (a+1, b+1) - (c+1, d+1)
    def sumRegion(self, a: int, b: int, c: int, d: int) -> int:
        c += 1
        d += 1
        return self.matrix[c][d]-self.matrix[c][b]-self.matrix[a][d]+self.matrix[a][b]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)