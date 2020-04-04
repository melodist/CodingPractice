"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
If a integer is not happy, happy value circulates.
"""
class Solution:
    def happy(self, n):
        answer = 0
        while n != 0:
            answer += (n % 10) ** 2
            n //= 10
        
        return answer
        
    def isHappy(self, n: int) -> bool:
        dic = {n:0}
        while True:
            n = self.happy(n)
            if n == 1: return True
            elif n in dic:
                return False
            else:
                dic[n] = 0
        
