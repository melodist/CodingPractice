"""
https://www.hackerrank.com/challenges/find-the-running-median/problem
Using min heap and max heap
min heap contains elements bigger than previous median
max heap contains elements smaller than or equal to previous median
If bigger heap has more than one element than smaller heap, 
push one element from bigger heap to smaller heap
"""
import heapq


def runningMedian(a):
    n = len(a)
    if n == 1:
        return [a[0] / 10 * 10]

    less_equal = [-min(a[0:2])]
    greater = [max(a[0:2])]
    result = [a[0] / 10 * 10, (a[0]+a[1])/2 / 10 * 10]
    
    for i in range(2, n):
        median = result[-1]

        if a[i] <= median:
            heapq.heappush(less_equal, -a[i])
            if len(less_equal) - len(greater) > 1:
                heapq.heappush(greater, -heapq.heappop(less_equal))
        else:
            heapq.heappush(greater, a[i])
            if len(greater) - len(less_equal) > 1:
                heapq.heappush(less_equal, -heapq.heappop(greater))

        
        if len(less_equal) == len(greater):
            temp = (greater[0] - less_equal[0]) / 2
        elif len(less_equal) > len(greater):
            temp = -less_equal[0]
        else:
            temp = greater[0]

        result.append(temp / 10 * 10)

    return result
