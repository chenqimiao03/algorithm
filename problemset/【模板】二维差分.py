n, m, q = list(map(int, input().strip().split()))

arr = [[0 for i in range(m + 2)] for j in range(n + 2)]

nums = []


def add(arr, a, b, c, d, k):
    arr[a][b] += k
    arr[a][d + 1] -= k
    arr[c + 1][b] -= k
    arr[c + 1][d + 1] += k


def build(arr, n, m):
    # 用了一圈 0 包裹着真实数据
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] += arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1]


for i in range(n):
    # 原数据也可以直接在 arr 上做差分，位置从 (1, j) 到 (i, j) 的区域
    nums.append(list(map(int, input().strip().split())))

for i in range(q):
    a, b, c, d, k = list(map(int, input().strip().split()))
    add(arr, a, b, c, d, k)

build(arr, n, m)

for i in range(n):
    for j in range(m):
        print(nums[i][j] + arr[i + 1][j + 1], end=' ')
    print()
