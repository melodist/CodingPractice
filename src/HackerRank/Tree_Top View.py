"""
https://www.hackerrank.com/challenges/tree-top-view/problem
"""
from collections import deque

def topView(root):
    #Write your code here
    dist = {}
    dist[0] = root.info

    q = deque([(root, 0)])
    while q:
        cur, d = q.popleft()

        if cur.left:
            q.append((cur.left, d-1))
            if d-1 not in dist:
                dist[d-1] = cur.left.info
        
        if cur.right:
            q.append((cur.right, d+1))
            if d+1 not in dist:
                dist[d+1] = cur.right.info

    ans = []
    for i in sorted(dist.keys()):
        ans.append(str(dist[i]))

    print(' '.join(ans))
