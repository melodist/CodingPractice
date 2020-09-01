"""
https://www.hackerrank.com/challenges/kingdom-division/problem
Using Sibling Dynamic Programming
"""
from collections import defaultdict, Counter, deque


def kingdomDivision(n, roads):
    edges = defaultdict(set)  # adjacency list
    degree = Counter()  # node degree
    for u, v in roads:
        edges[u].add(v)
        edges[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # The possible divisions for a sub-tree rooted @ node is
    #   count[node][parent]
    # where parent = True if the node shares its parent's color
    count = {u: {True: 1, False: 1} for u in degree}

    # We accumulate counts by iteratively stripping leaves from the tree
    leaves = deque([u for u in degree if degree[u] == 1])
    while True:
        node = leaves.popleft()

        # If parent differs, exclude case where ALL children differ
        count[node][False] = count[node][True] - count[node][False] 

        # If no edges left, we have reached root and are done
        if not degree[node]:
            root = node
            break
        else:
            # Otherwise update parent:
            parent = edges[node].pop()

            # update topology
            edges[parent].discard(node)
            degree[parent] -= 1
            if degree[parent] == 1:
                leaves.append(parent)

            # update counts
            count[parent][True] *= count[node][True] + count[node][False]
            count[parent][False] *= count[node][False]

    # Note each division has a corresponding one with colors switched
    total = 2 * count[root][0]
    return total % (10**9 + 7)
