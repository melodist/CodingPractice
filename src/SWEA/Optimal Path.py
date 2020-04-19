"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
TSP(Traveling Salesman Problem)
Dynamic Programming, Bitmask 이용.
"""
T = int(input())

def TSP(cur, visited):
    if dp[visited][cur]:
        return dp[visited][cur]
     
    # 모든 정점을 방문했을 경우 방문한 지점 - 집 사이의 거리를 반환함.
    if visited == (1<<n) - 1:
        return dist[cur+2][1]
         
    temp = float('inf')
    for i in range(n):
        if not visited & 1<<i:
            temp = min(temp, TSP(i, visited | 1<<i) + dist[cur+2][i+2]) # visited | 1<<i == visited + 1<<i
             
    dp[visited][cur] = temp
    return temp
     
for test_case in range(1, T+1):
    n = int(input())
    m = list(map(int, input().split()))
    x = m[::2]
    y = m[1::2]
     
    dp = [[0] * n for _ in range(1<<n)]
    dist = [[0] * (n+2) for _ in range(n+2)]
     
    for i in range(n+2):
        for j in range(n+2):
            dist[i][j] = abs(x[i] - x[j]) + abs(y[i] - y[j])
             
    for i in range(n):
        TSP(i, 0)
        dp[0][i] += dist[i+2][0]
    print(f'#{test_case} {min(dp[0])}')
 
