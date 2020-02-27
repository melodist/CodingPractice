"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""
def bfs(computers, visited, start):
    queue = [start]
    while queue:
        # curr = stack.pop() in dfs
        curr = queue.pop(0)
        if visited[curr] == 0:
            visited[curr] = 1
        for i in range(0, len(computers)):
            if computers[curr][i] == 1 and visited[i] == 0:
                queue.append(i)


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]  

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            bfs(computers, visited, i)     
            answer += 1
        i += 1

    return answer
