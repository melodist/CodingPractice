"""
https://www.acmicpc.net/problem/16922
4^20 -> 20^4
Count the numbers of roman numbers used for each value
cf. 100 = 50 * 10 = 50 + 10 + 5 * 8
"""
N = int(input())
arr = [1, 5, 10, 50]
visited = {}

def generate(i, p, total):
    if i == 3:
        temp = p + (N - total) * arr[i]
        visited[temp] = 0
        return
        
    for j in range(N - total + 1):
        generate(i+1, p + j * arr[i], total + j)
        
generate(0, 0, 0)
print(len(visited))
