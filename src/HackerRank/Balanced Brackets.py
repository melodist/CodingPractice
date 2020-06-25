"""
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
def isBalanced(s):
    balance = {'{' : '}', '(' : ')', '[' : ']'}
    stack = []

    for c in s:
        if c in balance:
            stack.append(c)
        else:
            if not stack or c != balance[stack.pop()]:
                return 'NO'
    
    return 'NO' if stack else 'YES'
