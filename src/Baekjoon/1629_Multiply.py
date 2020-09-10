"""
https://www.acmicpc.net/problem/1629
Using divide and conquer
MOD(a^2 % b) = MOD(a % b) ** 2
"""
#1. My Solution
def divide(a, b, c):
    d, e = divmod(b, 2)
    if b == 0:
        return 1
    elif b == 1:
        return a % c  # Note the case if b == 1
        
    return (((divide(a, d, c)) ** 2) * divide(a, e, c)) % c


a, b, c = map(int, input().split())
print(divide(a, b, c))

#2. Other Solution
# Return x to the power y; if z is present, return x to the power y, modulo z 
# (computed more efficiently than pow(x, y) % z)
print(pow(*map(int,input().split())))
