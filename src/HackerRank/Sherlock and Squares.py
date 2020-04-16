"""
https://www.hackerrank.com/challenges/sherlock-and-squares/problem
Using lambda for effective coding
"""
def squares(a, b):
    root_a, root_b = map(lambda s: int(math.sqrt(s)), [a-1,b])
    return root_b - root_a
