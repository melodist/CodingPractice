"""
https://programmers.co.kr/learn/courses/30/lessons/72416
Using Dynamic Programming and DFS
"""
#1. My Soltuion
from collections import defaultdict

def solution(sales, links):
    def dfs(start):
        for k in tree[start]:
            sum_child[start] += dfs(k)

        d[start][1] = sales[start-1] + sum_child[start]
        
        # Find d[start][0], which does not include start. So it should include minimum d[k][1]
        # if min(temp) is 0, sum_child[start] contains at least one subtree that contains a child node of start
        temp = [0 if d[k][0] > d[k][1] else d[k][1] - d[k][0] for k in tree[start]]

        if temp:
            d[start][0] = sum_child[start] + min(temp)
        else:  # if start is leaf node
            d[start][0] = sum_child[start]

        return min(d[start][0], d[start][1])

    answer = 0
    n = len(sales)
    tree = defaultdict(list)

    for u, v in links:
        tree[u].append(v)

    sum_child = [0] * (n+1)  # Find sum of minimum value for subtrees whose root is children of each node
    d = [[0] * 2 for _ in range(n+1)]  # 2D-dp array dp[i][1] means including i-th node

    return dfs(1)

#2. Other Solution
import functools


def solution(sales, links):

    @functools.lru_cache(maxsize=None)  # https://docs.python.org/ko/3/library/functools.html. Hashes return value for functions
    def min_sales(node, should_include_root):
        children_sum = sum(min_sales(c, False) for c in children[node])
        sales_including_root = sales[node] + children_sum
        if should_include_root:
            return sales_including_root
        sales_without_root = children_sum + min(
            (min_sales(c, True) - min_sales(c, False) for c in children[node]),
            default=0)
        return min(sales_including_root, sales_without_root)

    children = [[] for _ in sales]
    for a, b in links:
        children[a - 1].append(b - 1)
    return min(min_sales(0, True), min_sales(0, False))
  
