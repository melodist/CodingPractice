"""
https://www.hackerrank.com/challenges/journey-to-the-moon/problem
Using BFS and factorial
"""
#1. My Solution
from functools import reduce
from collections import defaultdict, deque


def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))


def journeyToMoon(n, astronaut):
    answer = n * (n-1) // 2
    graph = defaultdict(list)
    country = [-1] * n
    count = defaultdict(int)

    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)
        
    c = 0
    for i in range(n):
        if country[i] != -1:
            continue
        
        q = deque([i+1])
        country[i] = c
        count[c] += 1

        while q:
            cur = q.popleft()
            for u in graph[cur]:
                if country[u-1] == -1:
                    country[u-1] = c
                    count[c] += 1
                    q.append(u)

        c += 1

    for c in count.values():
        answer -= c * (c - 1) // 2

    return answer
    
#2. Other Solution
def journeyToMoon(n, astronaut):
    lis_of_sets = []
        
    for a, b in astronaut:
        indices = []
        new_set = set()
        set_len = len(lis_of_sets)
        s = 0
        while s < set_len:
            if a in lis_of_sets[s] or b in lis_of_sets[s]:
                indices.append(s)
                new_set = new_set.union(lis_of_sets[s])
                del lis_of_sets[s]
                set_len -= 1
            else:
                s += 1
        
        new_set = new_set.union([a, b])
        
        lis_of_sets.append(new_set)
        
    answer = n*(n-1)/2
    for i in lis_of_sets:
        answer -= len(i)*(len(i)-1)/2
        
    return answer
