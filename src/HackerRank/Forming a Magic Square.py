"""
https://www.hackerrank.com/challenges/magic-square-forming/problem
Magic Square의 경우의 수는 8가지.
8가지 경우의 수를 전부 구한 다음 s를 대입하여 magic square를 만드는 최소값을 구한다.
"""

def rotate_90(s):
    size = len(s)
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[i][j] = s[j][size-1-i]
    return temp

def rotate_180(s):
    size = len(s)
    temp = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            temp[i][j] = s[size-1-i][size-1-j]
    return temp

def rotate_270(s):
    size = len(s)
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[i][j] = s[size-1-j][i]
    return temp

def fliplr(s):
    size = len(s)
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[i][j] = s[size-1-i][j]
    return temp

def calc(s1, s2):
    answer = 0
    size = len(s1)
    for i in range(size):
        for j in range(size):
            answer += abs(s1[i][j] - s2[i][j])
    return answer 

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    s0 = [[8, 1 ,6], 
        [3, 5, 7], 
        [4, 9, 2]]
    s1 = rotate_90(s0)
    s2 = rotate_180(s0)
    s3 = rotate_270(s0)
    s4 = fliplr(s0)
    s5 = rotate_90(s4)
    s6 = rotate_180(s4)
    s7 = rotate_270(s4)

    temp = [calc(s, s0), calc(s, s1), calc(s, s2), calc(s, s3),
    calc(s, s4), calc(s, s5), calc(s, s6), calc(s, s7)]

    return min(temp)


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
