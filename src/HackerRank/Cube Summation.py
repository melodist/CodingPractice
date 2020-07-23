"""
https://www.hackerrank.com/challenges/cube-summation/problem
"""
#1. My Solution
for t in range(int(input())):
    n, m = map(int, input().split())
    hashmap = {}
    for _ in range(m):
        codes = input().split()
        if codes[0] == 'UPDATE':
            a, b, c = map(int, codes[1:4])
            hashmap[(a, b, c)] = int(codes[4])
        else:
            x1, y1, z1 = map(int, codes[1:4])
            x2, y2, z2 = map(int, codes[4:])
            answer = 0
            for a, b, c in hashmap:
                if x1 <= a <= x2 and y1 <= b <= y2 and z1 <= c <= z2:
                    answer += hashmap[(a, b, c)]
            print(answer)
            
#2. Other Solution using fenwick tree
def update(n, x, y, z, val):
    while z <= n:
        x1 = x
        while x1 <= n:
            y1 = y
            while y1 <= n:
                matrix[x1][y1][z] += val
                y1 += y1 & -y1
            x1 += x1 & -x1
        z += z & -z

def calculate_sum(x, y, z):
    sum = 0
    while z>0:
        x1=x
        while x1>0:
            y1=y
            while y1>0:
                sum += matrix[x1][y1][z]
                y1-= y1 & -y1
            x1 -= x1 & -x1
        z -= z & -z
    return sum

for t in range(int(input())):
    n, m = map(int, input().split())
    matrix = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    
    for _ in range(m):
        codes = input().split()
        if codes[0] == 'UPDATE':
            x, y, z = map(int, codes[1:4])
            x0, y0, z0 = x, y, z

            value1 = calculate_sum(x,y,z)- calculate_sum(x0-1,y,z) \
                    - calculate_sum(x,y0-1,z) + calculate_sum(x0-1,y0-1,z)
            value2 = calculate_sum(x,y,z0-1) - calculate_sum(x0-1,y,z0-1) \
                    - calculate_sum(x,y0-1,z0-1)  + calculate_sum(x0-1,y0-1,z0-1)
                    
            update(n, x, y, z, int(codes[4]) - (value1 - value2))
        else:
            x0, y0, z0 = map(int, codes[1:4])
            x, y, z = map(int, codes[4:])
            
            value1 = calculate_sum(x,y,z)- calculate_sum(x0-1,y,z) \
                    - calculate_sum(x,y0-1,z) + calculate_sum(x0-1,y0-1,z)
            value2 = calculate_sum(x,y,z0-1) - calculate_sum(x0-1,y,z0-1) \
                    - calculate_sum(x,y0-1,z0-1)  + calculate_sum(x0-1,y0-1,z0-1)
                    
            answer = value1 - value2
            print(answer)
