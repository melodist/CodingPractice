"""
https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""
def cutTheSticks(arr):
    N = len(arr)
    val = [0] * 1001
    for i in arr:
        val[i] += 1
    
    answer = [N]
    counter = N
    for i in val:
        if i > 0:
            counter -= i
            answer.append(counter)
            
    # Remove last value
    answer.pop()

    return answer
