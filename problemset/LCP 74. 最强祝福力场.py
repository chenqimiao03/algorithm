class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        # 二维差分 + 离散化
        # 排序 + 去重
        def _sort(arr):
            arr.sort()
            size = 1
            for i in range(1, len(arr)):
                if arr[i] != arr[size - 1]:
                    arr[size] = arr[i]
                    size += 1
            return size
        # 二分查找
        def rank(arr, v, size):
            l, r = 0, size - 1
            ret = 0
            while l <= r:
                m = (l + r) // 2
                if arr[m] >= v:
                    ret = m
                    r = m - 1
                else:
                    l = m + 1
            return ret + 1
        
        def add(arr, a, b, c, d, k=1):
            arr[a][b] += k
            arr[a][d + 1] -= k
            arr[c + 1][b] -= k
            arr[c + 1][d + 1] += k
        
        n = len(forceField)
        xs = [0 for i in range(n << 1)]
        ys = [0 for i in range(n << 1)]
        k, p = 0, 0
        for i in range(n):
            x, y, r = forceField[i][0], forceField[i][1], forceField[i][2]
            xs[k] = (x << 1) - r
            k += 1
            xs[k] = (x << 1) + r
            k += 1
            ys[p] = (y << 1) - r
            p += 1
            ys[p] = (y << 1) + r
            p += 1
        sizex = _sort(xs)
        sizey = _sort(ys)
        diff = [[0 for i in range(sizey + 2)] for j in range(sizex + 2)]
        for i in range(n):
            x, y, r = forceField[i][0], forceField[i][1], forceField[i][2]
            # 也可以使用哈希表
            a = rank(xs, (x << 1) - r, sizex)
            b = rank(ys, (y << 1) - r, sizey)
            c = rank(xs, (x << 1) + r, sizex)
            d = rank(ys, (y << 1) + r, sizey)
            add(diff, a, b, c, d)
        ret = 0
        for i in range(1, len(diff)):
            for j in range(1, len(diff[0])):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
                ret = max(ret, diff[i][j])
        return ret