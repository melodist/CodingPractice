"""
https://school.programmers.co.kr/learn/courses/30/lessons/178871
Implementation Problem
"""
#1. My Solution
def solution(players, callings):
    rank_for_players = {key:val for key, val in enumerate(players)}
    players_rank = {key:val for val, key in enumerate(players)}
    
    for c in callings:
        i = players_rank[c]
        d = rank_for_players[i-1]
        
        players_rank[c] -= 1
        players_rank[d] += 1
        
        rank_for_players[i] = d
        rank_for_players[i-1] = c
        
    answer = [''] * len(players)
    for p, k in players_rank.items():
        answer[k] = p
        
    return answer

#2. Other Solution
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players
