"""
https://programmers.co.kr/learn/courses/30/lessons/77485
Implementation Problem
"""
#1. My Solution
def solution(rows, columns, queries):
    answer = []
    
    # 행렬 초기화
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + (j+1)
    
    for x1, y1, x2, y2 in queries:
        arr_temp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                arr_temp[i][j] = arr[i][j]
                
        orders = []
        min_temp = float('inf')
        # 위
        for i in range(x1, x2):
            orders.append((y1-1, i-1))

        # 오른쪽
        for i in range(y1, y2):
            orders.append((i-1, x2-1))
            
        # 아래
        for i in range(x2, x1, -1):
            orders.append((y2-1, i-1))

        # 왼쪽
        for i in range(y2, y1, -1):
            orders.append((i-1, x1-1))
            
        orders_re = orders[1:] + [orders[0]]
        
        # 회전
        for (y1, x1), (y2, x2) in zip(orders, orders_re):
            arr_temp[y2][x2] = arr[y1][x1]
            min_temp = min(min_temp, arr[y1][x1])
        
        # 복사
        arr = arr_temp
        
        answer.append(min_temp)
    return answer
