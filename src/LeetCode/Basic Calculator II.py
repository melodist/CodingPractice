"""
https://leetcode.com/problems/basic-calculator-ii
Using stack
"""
#1. My Solution (534ms)
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = '+'
        stack = []
        for i, c in enumerate(s):
            print(c, num, sign)
            if c.isdigit():
                num = 10 * num + int(c)

            if not (c.isdigit() or c.isspace()) or i == len(s) - 1:
                match sign:
                    case '+':
                        stack.append(num)
                    case '-':
                        stack.append(-num)
                    case '*':
                        pre = stack.pop()
                        stack.append(pre * num)
                    case '/':
                        pre = stack.pop()
                        stack.append(int(pre / num))

                sign = c
                num = 0

        res = 0
        while stack:
            res += stack.pop()

        return res

#2. Other Solution (107ms)
class Solution:
    def calculate(self, s: str) -> int:
        res = ""
        stack = []
        operator = '+'
        for char in s + "+":
            if char in ['+', '-', '*', '/']:
                num2 = int(res)
                if operator == '+':
                    stack.append(num2)
                elif operator == '-':
                    stack.append(-num2)
                elif operator == '*':
                    stack.append(stack.pop() * num2)
                else:
                    stack.append(int(stack.pop()/num2))
                operator = char
                res = ""
            else:
                res += char
        return sum(stack)
