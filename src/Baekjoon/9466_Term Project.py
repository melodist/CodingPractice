"""
https://www.acmicpc.net/problem/9466
Using DFS
"""
#1. My Solution (5140ms)
import sys 


input = sys.stdin.readline
for _ in range(int(input())): 
    n = int(input()) 
    choice = [0] + [*map(int, input().split())]
    visit = [0] * (n+1)
    
    group = 1 
    for i in range(1, n+1): 
        if visit[i] == 0: 
            while visit[i] == 0: 
                visit[i] = group 
                i = choice[i] 
            while visit[i] == group: 
                visit[i] = -1 
                i = choice[i] 
            group += 1 
            
    cnt = 0
    for v in visit: 
        if v > 0: 
            cnt += 1 
    sys.stdout.write("{}\n".format(cnt))
    
#2. Other Solution (2512ms)
for _ in range(int(input())):
	n = int(input())
	ind, ck = [0] * (n+1), [0] * (n+1)  
	h,r = 0,0
	nxt = [0] + list(map(int,input().split()))
	for i in nxt:
		ind[i] += 1  # ind records counts in nxt 
	for i in range(1,n+1):
		h = i
		while ind[h] == 0 and ck[h] == 0:  # only find starting point
			ck[h] = 1  # if h appears again, there will be a cycle
			ind[nxt[h]] -= 1
			h = nxt[h]
			r += 1
	print(r)
