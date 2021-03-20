"""
https://www.hackerrank.com/challenges/count-triplets-1/problem
Using Dictionary
"""
#1. My Solution
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
