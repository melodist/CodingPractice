"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
Implementation Problem
"""
#1. My Solution
def dayOfProgrammer(year):
    # 256th day of the year
    if year == 1918:
        return '26.09.1918'
    if year < 1918:
        return '12.09.' + str(year) if year % 4 == 0 else '13.09.' + str(year)
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return '12.09.' + str(year)
            else:
                return '13.09.' + str(year)
        elif year % 4 == 0:
            return '12.09.' + str(year)
        else:
            return '13.09.' + str(year)
