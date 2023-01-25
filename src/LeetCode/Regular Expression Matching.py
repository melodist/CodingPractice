"""
https://leetcode.com/problems/regular-expression-matching
Using Dynamic Programming
"""
#1. My Solution (55ms)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        # dp(i, j) means s[i:] matches p[j:]
        def dp(i, j):
            print(i, j)

            m = len(s)
            n = len(p)
            if j == n:
                return i == m

            if i == m:
                # check wild card
                if (n-j) % 2 == 1:
                    return False
                # pattern should be 'a*b*c*'    
                for j in range(j, n-1, 2):
                    if p[j+1] != '*':
                        return False
                return True

            # memoization
            if (i, j) in memo: return memo[(i, j)]

            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < n - 1 and p[j+1] == '*':
                    # wild card matches more than 0
                    res = dp(i+1, j) or dp(i, j+2)
                else:
                    res = dp(i+1, j+1)
            else:
                if j < n - 1 and p[j+1] == '*':
                    # wild card matches 0
                    res = dp(i, j+2)

            memo[(i, j)] = res

            return res

        return dp(0, 0)
