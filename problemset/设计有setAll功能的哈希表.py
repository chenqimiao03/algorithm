"""
验证链接：https://www.nowcoder.com/questionTerminal/7c4559f138e74ceb9ba57d76fd169967
"""
n = int(input())
hashSet = {}
setAllTime = -1
setAllValue = 0
cnt = 0
for _ in range(n):
    a = list(map(int, input().strip().split()))
    # 设置操作
    if a[0] == 1:
        key, value = a[1], a[2]
        hashSet[key] = {'value': value, 'time': cnt}
        cnt += 1
    elif a[0] == 2:
        key = a[1]
        # 当前 key 不在哈希表中
        if key not in hashSet:
            print(-1)
        else:
            value = hashSet.get(key).get('value')
            time = hashSet.get(key).get('time')
            # 看到底是取 setAllValue 还是 value 看设置 value 的时间节点
            if time < setAllTime:
                print(setAllValue)
            else:
                print(value)
    elif a[0] == 3:
        value = a[1]
        setAllTime = cnt
        setAllValue = value
        cnt += 1
