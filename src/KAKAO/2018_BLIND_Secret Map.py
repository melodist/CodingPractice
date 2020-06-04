"""
https://programmers.co.kr/learn/courses/30/lessons/17681
"""
#1. My solution
def solution(n, arr1, arr2):
    board1 = []
    board2 = []

    for x in arr1:
        a = format(x, 'b')
        b = "0" * (n - len(a)) + a
        board1.append(b)

    for x in arr2:
        a = format(x, 'b')
        b = "0" * (n - len(a)) + a
        board2.append(b)

    ans = []
    for i in range(n):
        temp = ""
        for j in range(n):
            if board1[i][j] == '1' or board2[i][j] == '1':
                temp += "#"
            else:
                temp += " "
        ans.append(temp)

    return ans
    
#2. Using bit calculation ans rjust
def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        a = str(bin(x|y)[2:])
        a12 = a.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer
