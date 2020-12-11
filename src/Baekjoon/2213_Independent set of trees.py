"""
https://www.acmicpc.net/problem/2213
Using dynamic programming of tree
"""
#1. My Solution (1588ms)
import sys


def solve(u, p, flag):
    if flag:
        ans = a[u]
        arr = [u]
        for v in g[u]:
            if v == p:
                continue
            temp_ans, temp_arr = solve(v, u, 0)
            ans += temp_ans
            arr += temp_arr
    else:
        ans = 0
        arr = []
        for v in g[u]:
            if v == p:
                continue
            v_0, a_0 = solve(v, u, 0)
            v_1, a_1 = solve(v, u, 1)
            if v_0 < v_1:
                arr += a_1
                ans += v_1
            else:
                arr += a_0
                ans += v_0
        
    return ans, arr
    

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
g = [set() for _ in range(n+1)]

for r in sys.stdin.readlines():
    u, v = map(int, r.strip().split())
    g[u].add(v)
    g[v].add(u)

    
a_0, arr_0 = solve(1, 0, 0)
a_1, arr_1 = solve(1, 0, 1)

if a_0 > a_1:
    print(a_0)
    arr_0.sort()
    print(' '.join(map(str, arr_0)))
else:
    print(a_1)
    arr_1.sort()
    print(' '.join(map(str, arr_1)))
    
#2. Other Solution (84ms)
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
w=[0]+[*map(int,input().split())]
adj=[[] for _ in range(n+1)]

for _ in range(n-1):
  u,v=map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)
  
visit=[0]*(n+1)  # visit all nodes at once
def find_max_ind(r):  
  m1=w[r]; m2=0
  ind1=[r]; ind2=[]
  visit[r]=1
  for s in adj[r]:
    if visit[s]==0:
      m11,m21,ind11,ind21=find_max_ind(s)
      m1+=m21; ind1+=ind21
      if m11>m21:
        m2+=m11; ind2+=ind11
      else:
        m2+=m21; ind2+=ind21
  return m1,m2,ind1,ind2
m1,m2,ind1,ind2=find_max_ind(1)
if m1>m2:
  print(m1); print(*sorted(ind1))
else:
  print(m2); print(*sorted(ind2))
