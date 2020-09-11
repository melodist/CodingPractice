"""
https://programmers.co.kr/learn/courses/30/lessons/60063
Implementation Problem
Decrease number of cases
Express two points as row, col, direction
"""
#1. My Solution
from collections import deque


class Robot():
    def __init__(self, board):
        self.board = board
        self.N = len(board)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
    def dtop(self, r, c, d):
        return r + self.directions[d][0], c + self.directions[d][1]
        
    def check(self, r, c, d):
        r2, c2 = self.dtop(r, c, d)
        a = 0 <= r < self.N and 0 <= c < self.N and self.board[r][c] == 0
        b = 0 <= r2 < self.N and 0 <= c2 < self.N and self.board[r2][c2] == 0
        return a and b
    
    def convert(self, r, c, d):
        if d == 2:
            return r, c-1, 0
        elif d == 3:
            return r-1, c, 1
        else:
            return r, c, d
            
    def next_move(self, r, c, d):
        # RDLU and rotate 1~4
        r2, c2 = self.dtop(r, c, d)
        
        answer = []
        
        for dr, dc in self.directions:
            if self.check(r+dr, c+dc, d):
                answer.append((r+dr, c+dc, d))
                if r == r2 and dc == 0:
                    answer.append((r, c, (d+dr) % 4))
                    answer.append((r2, c2, (d+dr) % 4))
                if c == c2 and dr == 0:
                    answer.append((r, c, (d-dc) % 4))
                    answer.append((r2, c2, (d-dc) % 4))
        return answer
    
    def solve(self):
        start = ((0, 0, 0), 0)
        q = deque([start])
        visited = set()
        while q:
            (r, c, d), time = q.popleft()
            r2, c2 = self.dtop(r, c, d)
            if (r, c) == (self.N-1, self.N-1) or (r2, c2) == (self.N-1, self.N-1):
                return time
            
            temp = []
            for r1, c1, d1 in self.next_move(r, c, d):
                temp.append((self.convert(r1, c1, d1)))
            for (r3, c3, d3) in set(temp) - visited:
                q.append(((r3, c3, d3), time+1))
                visited.add((r3, c3, d3))
            visited.add((r, c, d))
    
def solution(board):
    r = Robot(board)
    return r.solve()

#2. Former Solution
"""
각 좌표에서 이동할 수 있는 방법들을 그래프로 만들고  
그 그래프의 최소 경로를 BFS를 이용하여 구함  
그래프가 가진 정점의 갯수는 r * c * d  = N * N * 4   
d : 0 -> 오른쪽 / d : 1 -> 아래쪽 / d : 2 -> 왼쪽 / d : 3 -> 위쪽  
이동할 수 있는 경우의 수는 8가지
1. 상하좌우 4가지 : go_up, down, left, right
2. 왼쪽 부분 축으로 회전 2가지 : rot_Lclock, rot_Lcclock
3. 오른쪽 부분 축으로 회전 2가지 : rot_Rclock, rot_Rcclock
    * 회전하는 경우는 d 방향 축을 회전시킨 방향을 새로운 축으로 좌표를 만든다.

각각의 경우의 수를 각각의 정점에 대하여 확인  
1. 지도의 끝을 벗어나는지 확인
2. 막혀있는지 확인  

[r, c, d]를 key로 하는 dictionary로 그래프를 표현
"""
def make_point(robot):
    """ Return coordinate of robot
    """
    r1 = [robot[0],robot[1]]
    if robot[2] % 4 == 0:
        r2 = [robot[0], robot[1]+1]
    elif robot[2] == 1:
        r2 = [robot[0]+1, robot[1]]
    elif robot[2] == 2:
        r2 = [robot[0], robot[1]-1]
    else:
        r2 = [robot[0]-1, robot[1]]

    return r1, r2


def go_up(robot, board):
    """
    Check if robot can go up in the board
    """
    size = len(board) 
    r1, r2 = make_point(robot)

    # Check Edge of board
    if r1[0] - 1 >= 0 and r2[0] - 1 >= 0:
        # Check Blocked
        if board[r1[0]-1][r1[1]] == 0 and board[r2[0]-1][r2[1]] == 0:
            return True
        else:
            return False
    else:
        return False


def go_down(robot, board):
    size = len(board) 
    r1, r2 = make_point(robot)

    # Check r2 can exist
    r, c = r2
    if board[r][c] == 1:
        return False
    # Check Edge of board
    if r1[0] + 1 < size and r2[0] + 1 < size:
        # Check Blocked
        if board[r1[0]+1][r1[1]] == 0 and board[r2[0]+1][r2[1]] == 0:
            return True
        else:
            return False
    else:
        return False


def go_left(robot, board):
    size = len(board) 
    r1, r2 = make_point(robot)

    # Check r2 can exist
    r, c = r2
    if board[r][c] == 1:
        return False
    # Check Edge of board
    if r1[1] - 1 >= 0 and r2[1] - 1 >= 0:
        # Check Blocked
        if board[r1[0]][r1[1]-1] == 0 and board[r2[0]][r2[1]-1] == 0:
            return True
        else:
            return False
    else:
        return False


def go_right(robot, board):
    size = len(board) 
    r1, r2 = make_point(robot)

    # Check r2 can exist
    r, c = r2
    if board[r][c] == 1:
        return False
    # Check Edge of board
    if r1[1] + 1 < size and r2[1] + 1 < size:
        # Check Blocked
        if board[r1[0]][r1[1]+1] == 0 and board[r2[0]][r2[1]+1] == 0:
            return True
        else:
            return False
    else:
        return False


def rotate_point(robot, axis, rot):
    """ Return check points for lotation
        Rotation 반대 / Axis 반대일 경우 겹침
        Rotation 0 : clockwise / 1 : counter-clockwise
        Axis 0 : r,c / 1 : r,c,d
    """        
    r1, r2 = make_point(robot)
    d = robot[2] % 4
    num = (axis + rot) % 2
    table = [[[1,0],[-1,0]],[[0,-1],[0,1]],[[-1,0],[1,0]],[[0,1],[0,-1]]]
    r3 = [r1[0]+table[d][num][0], r1[1]+table[d][num][1]]
    r4 = [r2[0]+table[d][num][0], r2[1]+table[d][num][1]]
    return r1, r2, r3, r4


def rotate_check(robot, board, axis, rot):
    """ Check rotation of robot
    """

    size = len(board) 
    r1, r2, r3, r4 = rotate_point(robot, axis, rot)
    # Check r2 can exist
    r, c = r2
    if board[r][c] == 1:
        return False

    r = range(0, size)

    # Check Edge of board
    if r3[0] in r and r3[1] in r and r4[0] in r and r4[1] in r:
        # Check Blocked
        if board[r3[0]][r3[1]] == 0 and board[r4[0]][r4[1]] == 0:
            return True
        else:
            return False
    else:
        return False

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []
    visited = []
    while queue:
        n, path = queue.pop(0)
        n = convert(n)
        if n == goal[0] or n == goal[1]:
            result.append(path)
        else:
            temp = []
            try:
                for m in graph[n]:
                    temp.append(convert(m))

                for m in set(temp) - set(visited):
                        queue.append((m, path + [m]))
                        visited.append(m)
            except:
                continue
    return result


def convert(m):
    if m[2] == -1:
        return (m[0]-1, m[1], 1)
    elif m[2] == 2:
        return (m[0], m[1]-1, 0)
    elif m[2] == 3:
        return (m[0]-1, m[1], 1)
    elif m[2] == 4:
        return (m[0], m[1], 0)
    else:
        return m
        
def solution(board):
    """ Return check points for lotation
        rotate_point(robot, axis, rot):
        Rotation 반대 / Axis 반대일 경우 겹침
        Rotation 0 : clockwise / 1 : counter-clockwise
        Axis 0 : r,c / 1 : r,c,d
    """
    graph = {}
    N = len(board)
    ran = range(0,N)
    dir = range(0,2)
    goals = [(N-1, N-2, 0)), (N-2, N-1, 1)]
    for r in ran:
        for c in ran:
            for d in dir:
                # Check r2 is in board
                robot = (r,c,d)
                r1, r2 = make_point(robot)
                if r2[0] in ran and r2[1] in ran:
                    # Check r2 can exist
                    r2_r, r2_c = r2
                    if board[r2_r][r2_c] == 1:
                        continue

                    temp = []
                    # Check each cases
                    if go_up(robot, board): temp.append((r-1,c,d))
                    if go_down(robot, board): temp.append((r+1,c,d))
                    if go_left(robot, board): temp.append((r,c-1,d))
                    if go_right(robot, board): temp.append((r,c+1,d))
                    if rotate_check(robot, board, 0, 0): temp.append((r,c,d+1))
                    if rotate_check(robot, board, 0, 1): temp.append((r,c,d-1))
                    if rotate_check(robot, board, 1, 0): temp.append((r2_r,r2_c,d-1))
                    if rotate_check(robot, board, 1, 1): temp.append((r2_r,r2_c,d+1))
                    if temp == []:
                        continue
                    else:
                        graph[(r,c,d)] = set(temp)
                else:
                    continue
    
    return len(bfs_paths(graph, (0,0,0), goals)[0]) - 1
