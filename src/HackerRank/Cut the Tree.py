"""
https://www.hackerrank.com/challenges/cut-the-tree/problem
Make any node as a root and Store sum of weights for subtree using DFS.
"""
#1. Naive Solution - O(n^2)
from collections import defaultdict, deque


def cutTheTree(data, edges):
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

#2. Optimal Solution - O(n)
from collections import defaultdict


def cutTheTree(data, edges):
    # Make the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    n = len(data)
    sums = [0] * (n + 1)
    root = [0] * (n + 1) # Store the root for each node
    q = [1]
    visited = set()
    
    # Non-recursive DFS (Depth-First Search)
    while q:
        cur = q[-1] # Don't pop the vertex here

        temp = []
        for v in tree[cur]:
            if v not in visited:
                temp.append(v)
                root[v] = cur
        
        # Calculate the sum of the weights in subtree
        if not temp:
            for v in tree[cur]:
                if v != root[cur]:
                    sums[cur] += sums[v]
            sums[cur] += data[cur - 1]
            q.pop() # Pop the vertex only if we visited its children already

        q += temp

        visited.add(cur)

    answer = 10**10

    for i in range(1, n):
        # Calculate difference between two subtrees
        temp = abs(2 * sums[i+1] - sums[1])
        answer = min(temp, answer)

    return answer
