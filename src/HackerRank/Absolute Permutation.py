"""
https://www.hackerrank.com/challenges/absolute-permutation/
3 Cases.
#1. If k = 0 -> [1, ... ,n]
#2. If n is odd -> answer does not exist
#3. If n is even
#3-1. n % (2*k) == 0 -> Divide array with subarray of 2*K elements and shuffle.
#3-2. n % (2*k) != 0 -> answer does not exist
"""
def absolutePermutation(n, k):
    # First solution
    if k == 0: return list(range(1, n+1))
    ans = []
    visited = [0] * (n+1)
    for i in range(n):
        if  0 < i + 1 - k <= n and visited[i + 1 - k] == 0:
            ans.append(i + 1 - k)
            visited[i + 1 - k] = 1
        elif 0 < i + 1 + k <= n and visited[i + 1 + k] == 0:
            ans.append(i + 1 + k)
            visited[i + 1 + k] =1
        else:
            return [-1]

    return ans
    
    
from itertools import chain

def absolutePermutation(n, k):
    # Second solution
    if k == 0: return list(range(1, n+1))
    if n % 2 != 0 or n % (2*k) != 0: return [-1]
        
    return list(chain.from_iterable([list(range((2*i - 1)*k + 1, i*2*k+1)) + list(range((i-1)*(2*k)+1, (2*i - 1)*k + 1))  for i in range(1, n//(2*k)+1)]))
