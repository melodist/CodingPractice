"""
https://programmers.co.kr/learn/courses/30/lessons/42894/
"""
#1. My Solution
# 위에서 블록을 떨어뜨려서 없앨 수 있는 블록을 차례대로 제거
# 쌓여있는 블록의 좌표를 각각 구한 후 블록이 지워지는 사각형의 빈 좌표를 구함
# 각각의 블록에 대하여 사각형의 빈 좌표에 검은 블록을 채울 수 있는지 확인
# 지울 수 있는 블록을 지우고 더 이상 블록이 지워지지 않을 때까지 
from collections import defaultdict


def solution(board):
    def check(k):
        if k == 0: return False

        x = set()
        y = set()

        for u, v in blocks[k]:
            x.add(u)
            y.add(v)

        blanks = []
        for a in x:
            for b in y:
                if (a, b) not in blocks[k]:
                    blanks.append((a, b))

        for c, d in blanks:
            # c == max(x) : blocked by itself
            # peaks[d] != k : blocked by other blocks
            if c == max(x) or peaks[d] != k:
                return False

        return True


    def remove(r):
        for a, b in blocks[r]:
            board[a][b] = 0
        del blocks[r]


    n = len(board)
    m = len(board[0])
    blocks = defaultdict(list)

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                blocks[board[i][j]].append((i, j))

    answer_prev = -1
    answer = 0
    while answer_prev != answer:
        peaks = [0] * m
        for i, x in enumerate(zip(*board)):
            for j in x:
                if j != 0:
                    peaks[i] = j
                    break

        prev = 0
        removed = []

        for k in peaks:
            if prev != k and check(k):
                removed.append(k)
            prev = k

        for r in removed:
            remove(r)

        answer_prev = answer
        answer += len(removed)

    return answer
    
#2. Other Solution
# 위에서부터 검은 블록을 채운다.
# 보드의 한 칸 한 칸을 검사하면서 검은 블록을 채울 수 있는지 확인
# 검은 블록을 채운 뒤에는 그 칸을 포함한 6개의 칸을 삭제할 수 있는지 확인
# 6개의 칸을 삭제한 이후에 삭제한 칸을 그대로 둘지 검은 블록으로 채울지 결정
