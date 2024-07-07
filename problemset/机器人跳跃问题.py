n = int(input().strip())
heights = list(map(int, input().strip().split()))

h = max(heights)
l = 0 # 最小能量
r = h # 最大能量

ret = -1

def f(heights, e, h):
    """判断以当前的能量 e 是否能通关
    """
    for height in heights:
        # 能量增长变化
        if height > e:
            e -= (height - e)
        else:
            e += (e - height)
        if e < 0:
            return False
        # 剪枝，防止移除
        # 能量大于建筑最大值，一定能通关
        if e >= h:
            return True
    return True

while l <= r:
    m = l + ((r - l) >> 1)
    if f(heights, m, h):
        ret = m
        r = m - 1
    else:
        l = m + 1
print(ret)