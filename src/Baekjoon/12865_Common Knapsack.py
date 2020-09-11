"""
https://www.acmicpc.net/problem/12865
0/1 Knapsack Problem
Using dynamic programming
"""
#1. My Solution
import sys


n, k = map(int, input().split())
stuff = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    stuff.append((w, v))
    
curr = [0] * (k+1)
prev = [0] * (k+1)

# i : index for stuff
# j : limit weight for knapsack
for i in range(n):
    for j in range(1, k+1):
        if j >= stuff[i][0]:
            curr[j] = max(prev[j-stuff[i][0]] + stuff[i][1], prev[j])
        else:
            curr[j] = prev[j]
            
    curr, prev = prev, curr

print(prev[-1])

#2. Other Solution
n, k = map(int, input().split())
dp_dict = {0: 0}
for _ in range(n):
    weight, value = map(int, input().split())
    
    new_list = []
    for accu_weight, accu_value in dp_dict.items():
        if accu_weight + weight <= k:
            new_list.append((accu_weight + weight, accu_value + value))
    
    for new_weight, new_value in new_list:
        if dp_dict.get(new_weight, 0) < new_value:
            dp_dict[new_weight] = new_value

print(max(list(dp_dict.values())))
