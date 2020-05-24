"""
https://www.acmicpc.net/problem/14889
Break when prev and current makes whole set.
"""
from itertools import combinations

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))
    
def score(c):
    score = 0
    for i, j in combinations(c, 2):
        score += arr[i][j] + arr[j][i]
    return score
    
ans = 10E18
prev = []
for c in combinations([i for i in range(N)], N//2):
    if set(c) | set(prev) == set([i for i in range(N)]):
        break
    d = [i for i in range(N) if i not in c]
    ans = min(abs(score(c)-score(d)), ans)
    prev = c
    
print(ans)
