"""
https://leetcode.com/problems/generate-parentheses
Using backtracking
"""
#1. My Solution (33ms)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, track):
            if left < 0 or right < 0:
                return
            if right < left:
                return

            if left == 0 and right == 0:
                res.append(track)
                return

            backtrack(left-1, right, track+'(')
            backtrack(left, right-1, track+')')

        if n == 0: return []
        res = []
        backtrack(n, n, '')

        return res
    
#2. Other Solution (24ms)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n <= 0:
            ans.append("")
            return ans
        
        for i in range(n):
            ans1 = self.generateParenthesis(i)
            for s1 in ans1:
                ans2 = self.generateParenthesis(n - 1 - i)
                for s2 in ans2:
                    ans.append('(' + s1 + ')' + s2)
        
        return ans
