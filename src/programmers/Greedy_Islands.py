"""
https://programmers.co.kr/learn/courses/30/lessons/42861
탐욕법을 사용. 비용이 낮은 순으로 costs를 정렬한 후 섬을 연결하며
주어진 섬의 연결 여부는 DFS를 통하여 검사
"""
def check(start, end, paths):
    stack = [start]
    visited = [0 for x in range(len(paths))]

    while stack:
        i = stack.pop()
        visited[i] = 1
        for j in range(len(paths)):
            if paths[i][j] == 1 and visited[j] == 0:
                if end == j:
                    return True
                stack.append(j)

    return False

def solution(n, costs):
    costs.sort(key=lambda c: c[2])
    paths = [[0 for x in range(n)] for y in range(n)]
    answer = 0

    for cost in costs:
        a, b, c = cost

        if not check(a, b, paths):
            answer += c
            paths[a][b] = 1
            paths[b][a] = 1 # 섬이 서로 연결되어 있으므로
        else:
            continue
    return answer
