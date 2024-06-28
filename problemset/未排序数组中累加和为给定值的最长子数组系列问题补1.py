# 和题目【未排序数组中累加和为给定值的最长子数组长度】类似
n = int(input().strip())
nums = list(map(int, input().strip().split()))

for i in range(len(nums)):
    if nums[i] > 0:
        nums[i] = 1
    elif nums[i] == 0:
        continue
    else:
        nums[i] = -1

HashMap = {0: -1}
total, ret = 0, 0

for i in range(len(nums)):
    total += nums[i]
    if HashMap.get(total, None) is not None:
        ret = max(ret, i - HashMap.get(total))
    else:
        HashMap[total] = i
print(ret)
