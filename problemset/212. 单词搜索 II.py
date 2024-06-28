class Solution:

    def __init__(self) -> None:
        self._N = 80001
        self._tree = [[0 for i in range(26)] for j in range(self._N)]
        self._end = [None for i in range(self._N)]
        self._path = [0 for i in range(self._N)]
        self._cnt = 1
    
    def clear(self):
        for i in range(self._cnt):
            for j in range(26):
                self._tree[i][j] = 0
            self._end[i] = None
            self._path[i] = 0
        self._cnt = 1

    def build(self, words):
        self.clear()
        for word in words:
            self.insert(word)

    def insert(self, word):
        cur = 1
        self._path[cur] += 1
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if self._tree[cur][j] == 0:
                self._cnt += 1
                self._tree[cur][j] = self._cnt
            cur = self._tree[cur][j]
            self._path[cur] += 1
        self._end[cur] = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, row, col, t, ret):
            # 判断是否越界和当前的路是否走过
            if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or board[row][col] == 0:
                return 0
            tmp = board[row][col]
            road = ord(tmp) - ord('a')
            t = self._tree[t][road]
            if self._path[t] == 0:
                return 0
            fix = 0
            if self._end[t] is not None:
                fix += 1
                ret.append(self._end[t])
                self._end[t] = None
            # 标记当前路径已经走过
            board[row][col] = 0
            fix += dfs(board, row - 1, col, t, ret)
            fix += dfs(board, row + 1, col, t, ret)
            fix += dfs(board, row, col - 1, t, ret)
            fix += dfs(board, row, col + 1, t, ret)
            self._path[t] -= fix
            # 恢复现场
            board[row][col] = tmp
            return fix

        ret = []
        self.build(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(board, i, j, 1, ret)
        self.clear()
        return ret