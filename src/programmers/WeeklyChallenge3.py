"""
https://programmers.co.kr/learn/courses/30/lessons/84021
Implementation Problem
"""
from collections import deque


# 보드에서 블록 추출
def extract(board, val):
    # 블록 만들기
    def makeBlock(i, j):
        up = left = 0
        q = deque([(0, 0)])
        blocks = []
        answer = []
        
        # 연결된 칸 찾기
        while q:
            u, v = q.popleft()
            blocks.append((u, v))
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= i+di+u < n and 0 <= j+dj+v < n and not visited[i+di+u][j+dj+v] and board[i+u+di][j+v+dj] == val:
                    up = min(up, u+di)
                    left = min(left, v+dj)
                    visited[i+di+u][j+dj+v] = True
                    q.append((u+di, v+dj))
        
        # 왼쪽, 위가 (0,0)이 되도록
        for y, x in blocks:
            answer.append((y - up, x - left))
        
        # 순서 정렬
        return sorted(answer)
    
    ans = []
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == val and not visited[i][j]:
                visited[i][j] = True
                ans.append(makeBlock(i, j))
                
    return ans

# 블록 90도 회전
def rot90(block):
    maxY = 0
    maxX = 0

    for y, x in block:
        maxY = max(y, maxY)
        maxX = max(x, maxX)
        
    return sorted([(x, maxY - y) for y, x in block])

# 두 블록이 같은 블록인지 확인
def check(block1, block2):
    if len(block1) != len(block2):
        return False
    
    for a, b in zip(block1, block2):
        if a != b:
            return False

    return True

def solution(game_board, table):
    def solve(i, j, block):
        flag = True
        temp = 0
        
        for di, dj in block:
            if block[i+di][j+dj] == 1:
                flag = False
                break
        
        if flag:
            for di, dj in block:
                game_board[i+di][j+dj] = 1
                temp += 1
                
        return temp
                
    answer = 0
    # 빈 칸 추출 (r, c, 비트마스크)
    blanks = extract(game_board, 0)
    
    # 블록 추출
    blocks = extract(table, 1)

    # 빈 칸에 대해 블록 맞춰보기
    block_used = [False] * len(blocks)
    
    for blank in blanks:
        for i, block in enumerate(blocks):
            if block_used[i]:
                continue
                
            flag = False
            
            for _ in range(4):
                block = rot90(block)
                if check(block, blank):
                    flag = True
            
            # 맞는 블록일 경우 다른 블록을 검사하지 않고 종료
            if flag: 
                block_used[i] = True
                answer += len(block)
                break
                
    return answer
