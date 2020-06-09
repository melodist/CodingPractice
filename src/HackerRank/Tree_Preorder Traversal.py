"""
https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
"""
#1. Non-recursive Solution
def preOrder(root):
    stack = [root]
    ans = []
    while stack:
        cur = stack.pop()
        ans.append(str(cur))
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    print(' '.join(ans))
    
#2. Recursive Solution
def preOrder(root):
    if root:
        print(str(root), end=' ')
        preOrder(root.left)
        preOrder(root.right)
