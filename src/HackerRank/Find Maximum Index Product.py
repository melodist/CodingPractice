"""
https://www.hackerrank.com/challenges/find-maximum-index-product/problem
"""
#1. Solution Using Two Stacks
def solve(arr):
    """we keep a stack to access the next biggest in O(1)
    """
    stack_left, stack_right = [], []
    left, right = [], []

    # left -> right
    for i,e in enumerate(arr):
        while stack_left and e >= stack_left[-1][0]:
            stack_left.pop()
        left.append(stack_left[-1][1] if stack_left else 0)
        stack_left.append((e, i+1))

    # right -> left
    for i in reversed(range(len(arr))):
        while stack_right and arr[i] >= stack_right[-1][0]:
            stack_right.pop()
        right.append(stack_right[-1][1] if stack_right else 0)
        stack_right.append((arr[i], i+1))

    # multiply
    res = -float('inf')
    for i,e in enumerate(left):
        res = max(res, (left[i])*(right[len(right)-1 -i]))
    return res 
