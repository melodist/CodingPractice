"""
https://leetcode.com/problems/basic-calculator
Using recursion
"""
#1. My Solution (4692ms)
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = 10 * num + int(c)
                
                if c == '(':
                    num = helper(s)
                
                if not (c.isdigit() or c.isspace()) or len(s) == 0:
                    match sign:
                        case '+':
                            stack.append(num)
                        case '-':
                            stack.append(-num)
                    
                    num = 0
                    sign = c

                if c ==')': break

            return sum(stack)
        
        return helper(list(s))
      
#2. Other Solution (59ms)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        value = 0
        sign = 1
        for each in s:
            if each.isdigit():
                operand = (operand * 10) + int(each)    

            elif each == '+':
                value += sign * operand
                sign = 1
                operand = 0

            elif each == '-':
                value += sign * operand
                sign = -1
                operand = 0                                       
                                                    
            elif each == '(':
                stack.append(value)  
                stack.append(sign)        

                sign = 1
                value = 0

            elif each == ')':
                value += sign * operand
                value *= stack.pop()
                value += stack.pop()
                
                operand = 0

        return value + sign * operand
