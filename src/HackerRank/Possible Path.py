"""
https://www.hackerrank.com/challenges/possible-path
Mathematical Problem

By condition, x = a + mb and y = na + b
If gcd(a,b) = k, a = i * k, b = j * k
So, x = (i + j * m) * k, y = (i * n + j) * k
gcd(a,b) = gcd(x, y)
"""
#1. My Solution
def solve(a, b, x, y):
    gcd1 = math.gcd(a, b)
    gcd2 = math.gcd(x, y)
    if gcd1 == gcd2:
        return "YES"
    else:
        return "NO"
