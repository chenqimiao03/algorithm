#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 栈排序
# @param a int整型一维数组 描述入栈顺序
# @return int整型一维数组
#
class Solution:
    def solve(self , a):
        """时间复杂度：O(N^2)
        """
        # write code here
        def sort(stack):
            d = deep(stack)
            while d > 0:
                maxValue = MAX(stack, d)
                k = times(stack, d, maxValue)
                down(stack, d, maxValue, k)
                d -= k
            
        def deep(stack):
            """利用递归求栈的深度
            """
            if len(stack) == 0:
                return 0
            top = stack.pop()
            ret = deep(stack) + 1
            stack.append(top)
            return ret

        def MAX(stack, deep):
            """利用递归查找栈中的最大值
            """
            if deep == 0:
                return -2 ** 31
            num = stack.pop()
            ret = max(num, MAX(stack, deep - 1))
            stack.append(num)
            return ret
        
        def times(stack, d, maxValue):
            """利用递归统计栈中最大值出现的次数
            """
            ret = 0
            if d == 0:
                return ret
            num = stack.pop()
            ret += 1 if num == maxValue else 0
            ret += times(stack, d - 1, maxValue)
            stack.append(num)
            return ret
        
        def down(stack, d, maxValue, k):
            """利用递归将栈中的最大值下沉到栈底
            """
            if d == 0:
                while k:
                    stack.append(maxValue)
                    k -= 1
                return
            num = stack.pop()
            down(stack, d - 1, maxValue, k)
            if num != maxValue:
                stack.append(num)
            return
        sort(a)
        return a

print(Solution().solve([5, 1, 3, 2]))