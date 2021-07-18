"""
https://programmers.co.kr/learn/courses/30/lessons/81302
Implementation Problem
"""
#1. My Solution
def calc_dist(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])

def solution(places):
    answer = []
    
    for room in places:
        people = []
        flag  = 1
        
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    people.append((i, j))
                    
        for u in people:
            for v in people:
                if calc_dist(u, v) == 0:
                    continue
                elif calc_dist(u, v) == 1:
                    flag = 0
                    break
                elif calc_dist(u, v) == 2:
                    # 가로
                    if abs(u[0] - v[0]) == 2:
                        mid = (u[0] + v[0]) // 2
                        if room[mid][u[1]] == 'O':
                            flag = 0
                            break
                    # 세로
                    if abs(u[1] - v[1]) == 2:
                        mid = (u[1] + v[1]) // 2
                        if room[u[0]][mid] == 'O':
                            flag = 0
                            break
                            
                    # 대각선
                    if room[u[0]][v[1]] == 'O' or room[v[0]][u[1]] == 'O':
                        flag = 0
                        break
                    
        answer.append(flag)
                
    return answer
