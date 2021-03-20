"""
https://www.hackerrank.com/challenges/count-triplets-1/problem
Using Dictionary
"""
#1. My Solution
from collections import defaultdict


def countTriplets(arr, r):
    count = defaultdict(int)
    count2 = defaultdict(int)
    ans = 0
    for k in arr:
        if k % r == 0 and k // r in count2:  #  Countercase. k = 49, r = 4
            ans += count2[k // r]
        if k % r == 0 and k // r in count:
            count2[k] += count[k // r]
        count[k] += 1

    return ans

#2. Other Solution
def countTriplets(arr, r):
        count = 0
        dict = {}
        dictPairs = {}

        for i in reversed(arr):
                if i*r in dictPairs:
                        count += dictPairs[i*r]
                if i*r in dict:
                        dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

                dict[i] = dict.get(i, 0) + 1  # dict.get(i, x) returns x if i is not in dict

        return count
