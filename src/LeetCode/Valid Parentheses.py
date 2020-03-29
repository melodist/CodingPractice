"""
https://leetcode.com/problems/valid-parentheses/
Stack을 이용하여 괄호의 짝이 맞는지 비교하고
비교가 끝났을 때 Stack에 비어있지 않으면 False를 반환
"""
class Solution:
    def isValid(self, s: str) -> bool   
        if s == "": return True
        stack = []
        char_dict = {'(':')', '[' :']', '{':'}'}
        for char in s:
            if char in char_dict:
                stack.append(char)
            elif not stack: return False
            else:
                prev = stack.pop()
                if char_dict[prev] == char:
                    continue
                else:
                    return False
                
        if stack:
            return False
        else:                
            return True
