"""
https://www.hackerrank.com/challenges/candies/problem
Using Greedy Algorithm
Classify the children into four kinds - valley, rise, fall, peak
"""
def candies(n, arr):
    count = [1]
    for i,x in enumerate(arr[1:],1):
        if x <= arr[i-1]:
            count.append(1)  # fall
        else:
            count.append(count[i-1]+1)  # rise
    
    # enumerate(sequence, start=0)
    # x -> arr[n-2] <= arr[n-2+1] = arr[n-1]
    for i,x in enumerate(arr[-2::-1],2):
        if x <= arr[n-i+1]:
            count[n-i] = max(count[n-i], 1)  # valley
        else:
            count[n-i] = max(count[n-i], count[n-i+1]+1)  # peak

    return sum(count)
