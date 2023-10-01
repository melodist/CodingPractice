"""
https://leetcode.com/problems/add-binary/
Binary Addition Problem
"""
#1. Simple Solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

#2. Solution not using built-in functions
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry;
            if i >= 0 : sum += ord(a[i]) - ord('0') # ord is use to get value of ASCII character
            if j >= 0 : sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0;
            res += str(sum % 2)

        if carry != 0 : res += str(carry);
        return res[::-1]
