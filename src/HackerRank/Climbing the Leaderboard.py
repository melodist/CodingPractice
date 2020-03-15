"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/
Sort 함수 사용시 시간 초과가 발생하므로 이진 탐색을 사용하여 해결함.
target이 중간값보다 큰 경우와 작은 경우에 각각 발생하는 경우의 수가 다름에 유의.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    answer = []
    scores = list(set(scores))
    scores.sort(reverse=True)

    for a in alice:
        answer.append(binary_search(scores, a)+1)
        
    return answer

def binary_search(array, value):
    start = 0
    end = len(array) - 1
    
    while start < end:
        mid = (start + end) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            if array[mid - 1] == value:
                return mid - 1
            elif array[mid - 1] > value:
                return mid
            else:
                end = mid - 1
        else:
            if array[mid + 1] <= value:
                return mid + 1
            else:
                start = mid + 1
    
    if start == 0:
        return 0
    else:
        return len(array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
