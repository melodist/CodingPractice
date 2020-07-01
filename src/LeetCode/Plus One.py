"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
"""
#1. My Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1
        
        n = len(digits)
        for i in range(n-1):
            if digits[i] == 10:
                digits[i] -= 10
                digits[i+1] += 1
                
        if digits[n-1] == 10:
            digits[n-1] -= 10
            digits.append(1)
            
        return digits[::-1]
        
#2. Solution Using Carry
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        n = len(digits)
        carry = 1
        
        for i in range(n):
            digits[i] += carry
            carry = digits[i] // 10
            
            if carry:
                digits[i] = 0
            else:
                break
                
        if carry:
            digits.append(1)
            
        return digits[::-1]
