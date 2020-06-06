"""
https://programmers.co.kr/learn/courses/30/lessons/42896/
Reversed-DP
"""
def solution(left, right):
    l, r = len(left), len(right)
    arr = [[0] * (l+1) for i in range(r+1)]
    
    for i in reversed(range(r)):
        for j in reversed(range(l)):
            if left[j] > right[i]:
                arr[i][j] = arr[i+1][j] + right[i]
            else:
                arr[i][j] = max(arr[i+1][j+1], arr[i][j+1])
        
    return arr[0][0]
