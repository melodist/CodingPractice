"""
https://programmers.co.kr/learn/courses/30/lessons/64063
Using Hashmap and update visited nodes for each room number
"""
#1. My Solution
def solution(k, room_number):
    used = {}
    answer = []

    for r in room_number:
        temp = r
        visited = [temp]

        if temp not in used:
            used[temp] = temp + 1
        else:
            while temp in used:
                visited.append(used[temp])
                temp = used[temp]

            # Update visited nodes
            for v in visited:
                used[v] = temp + 1

        answer.append(temp)

    return answer
