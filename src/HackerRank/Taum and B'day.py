"""
https://www.hackerrank.com/challenges/taum-and-bday/problem
Find minimum for all cases.
1. Buy b black and w white
2. Buy all black: wc > bc + z
3. Buy all white: bc > wc + z
"""
# My Solution
def taumBday(b, w, bc, wc, z):
    # Write your code here
    if abs(bc - wc) <= z:
        return bc * b + wc * w
    else:
        if bc > wc: bc, wc, b, w = wc, bc, w, b
        return bc * (b + w) + z * w
        
# Optimal Solution
def taumBday(b, w, bc, wc, z):
    # Write your code here
    return min(b * bc + w * wc, b * bc + w * (bc + z), b * (wc + z) + w * wc)
