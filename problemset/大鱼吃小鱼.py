"""bilibili 笔试：https://www.nowcoder.com/practice/77199defc4b74b24b8ebf6244e1793de?tpId=196&tqId=37572&ru=/exam/oj
"""
n = int(input().strip())
nums = list(map(int, input().strip().split()))
stack = [] # 从右往左遍历，小压大
# 统计每个位置的鱼吃完后续的鱼需要经过几轮
ret = 0
for i in range(n - 1, -1, -1):
    # i 号鱼，权重 nums[i]
    cur = 0
    # 栈顶的鱼的权重比当前鱼的权重小，意味着当前的鱼能吃掉它
    while stack and stack[-1][0] < nums[i]:
        # 因为每次只能吃右边最近的的鱼，所以轮数依次加 1
        cur = max(cur + 1, stack.pop()[1])
    # 求到了，第 i 条鱼吃完后续的鱼需要几轮，然后将其放到栈中
    stack.append([nums[i], cur])
    ret = max(ret, cur)
print(ret)