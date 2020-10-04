"""
https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
Using greedy algorithm
"""
#1. My Solution
def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    numOfTransmitters = 0
    i = 0
    while i < n:
        numOfTransmitters += 1
        loc = x[i] + k
        
        # Find maximum coverage
        while i < n and x[i] <= loc:
            i += 1
        
        # Return to maximum coverage
        i -= 1
        
        # Find maximum coverage from center
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1

    return numOfTransmitters
