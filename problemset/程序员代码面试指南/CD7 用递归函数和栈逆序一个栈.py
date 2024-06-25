"""
时间复杂度：O(N^2)
"""
def reverse(stack):
    if len(stack) == 0:
        return
    buttom = buttomOut(stack)
    reverse(stack)
    stack.append(buttom)

def buttomOut(stack):
    """移除栈底元素
    """
    top = stack.pop()
    if len(stack) == 0:
        return top
    else:
        last = buttomOut(stack)
        stack.append(top)
        return last
stack = ['c', 'b', 'a']
reverse(stack)
print(stack)