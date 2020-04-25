"""
https://www.hackerrank.com/challenges/fair-rations/problem
"""
def fairRations(B):
    n = len(B)
    ans = 0
    for i in range(n-1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i+1] += 1
            ans += 2
        
    return ans if B[-1] % 2 == 0 else 'NO'
