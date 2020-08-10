"""
https://www.hackerrank.com/challenges/cut-the-tree/problem
"""
#1. My Solution
from collections import defaultdict, deque


def cutTheTree(data, edges):
    # Write your code here
    answer = 10**10
    for l, r in edges:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        left = 0
        q1 = deque([l])
        visited1 = set([l, r])
        while q1:
            cur = q1.popleft()
            left += data[cur-1]
            for v in tree[cur]:
                if v not in visited1:
                    q1.append(v)

            visited1.add(cur)

        right = 0
        q2 = deque([r])
        visited2 = set([l, r])
        while q2:
            cur = q2.popleft()
            right += data[cur-1]
            for v in tree[cur]:
                if v not in visited2:
                    q2.append(v)

            visited2.add(cur)

        answer = min(answer, abs(left - right))

    return answer

#2. Other Solution
sys.setrecursionlimit(10**5)

def dfs(conn , node, sums, data, parent):
    if sums[node]!=0:
        return sums[node]
    nb = conn[node]
    if len(nb)==1 and node!=0:
        sums[node] = data[node]
        return data[node]
    ans = 0
    for n1 in nb:
        if n1!=parent:
            ans += dfs(conn, n1, sums, data, node)
    ans += data[node]
    sums[node] = ans 
    return ans

def cutTheTree(data, edges):
    conn = [[] for i in range(n)]
    for e in edges:
        e1 = e[0]-1
        e2 = e[1]-1
        conn[e1].append(e2)
        conn[e2].append(e1)
    sums = [0 for i in range(n)]
    dfs(conn , 0, sums, data, 0)
    print(sums)
    mindiff = 999999999
    for i in range(1, n):
        ## seperate node i
        sum1 = sums[i]
        sum2 = sums[0] - sums[i]
        diff = abs(sum1 - sum2)
        mindiff = min(mindiff, diff)
    return mindiff
