"""
https://programmers.co.kr/learn/courses/30/lessons/81305
Using Parametric Search and Tree DP
"""
#1. My Solution
import sys
sys.setrecursionlimit(10**6)
cnt = 0

def solution(k, num, links):
    def solve(limit):
        global cnt
        cnt = 0
        dfs(root, limit)
        cnt += 1
        return cnt

    def dfs(node, limit):
        global cnt
        l, r = links[node]
        
        # Find left subtree maximum value
        lv = 0
        if l != -1: lv = dfs(l, limit)
            
        # Find right subtree maximum value
        rv = 0
        if r != -1: rv = dfs(r, limit)
            
        if (num[node] + lv + rv <= limit):
            return num[node] + lv + rv
        
        if num[node] + min(lv, rv) <= limit:
            cnt += 1
            return num[node] + min(lv, rv)
        
        cnt += 2
        return num[node]
        
    # find root
    n = len(num)
    p = [-1] * 10001 # parents for find root
    
    for i, (l, r) in enumerate(links):
        p[l] = p[r] = i
        
    root = 0
    for i in range(n):
        if p[i] == -1:
            root = i
            break        

    # parametric search
    left = max(num)
    right = sum(num)

    while left < right:
        mid = (left + right) // 2
        # If answer is smaller than k, find smaller value for answer
        if solve(mid) <= k:
            right = mid
        else:
            left = mid + 1
    return left

#2. Other Solution
import sys
sys.setrecursionlimit(10**6)

l = [0] * 10005 # 왼쪽 자식 노드 번호
r = [0] * 10005 # 오른쪽 자식 노드 번호
x = [0] * 10005 # 시험장의 응시 인원
p = [-1] * 10005 # 부모 노드 번호
n = 0 # 노드의 수
root = 0 # 루트

cnt = 0 # 그룹의 수

# cur : 현재 보는 노드 번호, lim : 그룹의 최대 인원 수
def dfs(cur, lim):
    global cnt
    lv = 0
    if l[cur] != -1: lv = dfs(l[cur], lim)
    rv = 0 # 오른쪽 자식 트리에서 넘어오는 인원 수
    if r[cur] != -1: rv = dfs(r[cur], lim)
    # 1. 왼쪽 자식 트리와 오른쪽 자식 트리에서 넘어오는 인원을 모두 합해도 lim 이하일 경우
    if x[cur] + lv + rv <= lim:
        return x[cur] + lv + rv
    # 2. 왼쪽 자식 트리와 오른쪽 자식 트리에서 넘어오는 인원 중 작은 것을 합해도 lim 이하일 경우
    if x[cur] + min(lv, rv) <= lim:
        cnt += 1 # 둘 중 큰 인원은 그룹을 지어버림
        return x[cur] + min(lv, rv)
    
    # 3. 1, 2 둘 다 아닐 경우
    cnt += 2 # 왼쪽 자식 트리와 오른쪽 자식 트리 각각을 따로 그룹을 만듬
    return x[cur]

def solve(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1 # 맨 마지막으로 남은 인원을 그룹을 지어야 함
    return cnt

def solution(k, num, links):
    global root
    n = len(num)
    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1: p[l[i]] = i
        if r[i] != -1: p[r[i]] = i
    
    for i in range(n):
        if p[i] == -1:
            root = i
            break
    st = max(x)
    en = 10 ** 8
    while st < en:
        mid = (st+en) // 2
        if solve(mid) <= k:
            en = mid
        else: st = mid+1    
    return st
