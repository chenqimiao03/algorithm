#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def foundMonotoneStack(self , nums: List[int]) -> List[List[int]]:
        # write code here
        stack = []
        n = len(nums)
        ret = [[0 for i in range(2)] for j in range(n)]
        for i in range(n):
            # 栈不是空并且栈顶元素的值大于等于当前的值
            # 值：栈顶->栈顶，大->小
            while stack and nums[stack[-1]] >= nums[i]:
                top = stack.pop()
                # 左边比 nums[top] 小的（距离最近的）
                ret[top][0] = stack[-1] if stack else -1
                # 右边比 nums[top] 小的（距离最近的）
                ret[top][1] = i
            stack.append(i)
        # 遍历完了，如果栈非空，那么栈中的元素在右边找不到更小的元素了，直接填写 -1
        while stack:
            top = stack.pop()
            ret[top][0] = stack[-1] if stack else -1
            ret[top][1] = -1
        # 修正阶段：左侧答案一定是正确的，不需要修正；右侧答案需要修正
        # nums[n - 1] 的右侧比它小的数一定是没有的
        for i in range(n - 2, -1, -1):
            if ret[i][1] != -1 and nums[ret[i][1]] == nums[i]:
                ret[i][1] = ret[ret[i][1]][1]
        return ret