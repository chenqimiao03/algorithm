n, m = list(map(int, input().strip().split()))
arr = [0 for i in range(100001)]

def set(arr, l, r, s, e, d):
    arr[l] += s
    arr[l + 1] += d - s
    arr[r + 1] -= d + e
    arr[r + 2] += e

def build(arr, n):
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]

for i in range(m):
    l, r, s, e = list(map(int, input().strip().split()))
    d = (e - s) // (r - l)
    set(arr, l, r, s, e, d)

build(arr, n)
maxValue = 0
xor = 0
for i in range(1, n + 1):
    xor ^= arr[i]
    maxValue = max(maxValue, arr[i])
print(xor, ' ', maxValue)