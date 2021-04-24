"""
https://www.acmicpc.net/problem/1133
Using Backtracking
"""
#1. My Solution (72ms)
def find_k(s):
    ns = len(s)
    visited = [[2] * ns for _ in range(ns)]
    ans = 2
    for i in range(ns-1):
        for j in range(1, (ns-i)//2+1):
            if s[i:i+j] == s[i+j:i+2*j]:
                visited[i+j][j] = visited[i][j] + 1
                ans = max(ans, visited[i+j][j])
                
    return ans

def backtracking(s):
    if len(s) == N:
        return s
        
    for i in range(A):
        c = chr(ord('A') + i)
        temp = s+c
        if find_k(temp) <= K:
            temp_ans = backtracking(temp)
            if temp_ans != -1:
                return temp_ans
    
    return -1

K, N, A = map(int, input().split())
print(backtracking("A"))
