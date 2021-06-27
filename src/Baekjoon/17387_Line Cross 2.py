"""
https://www.acmicpc.net/problem/17387
Using CCW(Counter-clockwise)
"""
#1. My Solution (68ms)
def ccw(x1, x2, x3, y1, y2, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - (y1 * x2 + y2 * x3 + y3 * x1)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw1 = ccw(x1, x2, x3, y1, y2, y3)
ccw2 = ccw(x1, x2, x4, y1, y2, y4)
ccw3 = ccw(x3, x4, x1, y3, y4, y1)
ccw4 = ccw(x3, x4, x2, y3, y4, y2)

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
    if p1 >= p2:
        p1, p2 = p2, p1
    if p3 >= p4:
        p3, p4 = p4, p3
        
    if p4 >= p1 and p2 >= p3:
        print(1)
    else:
        print(0)
        
elif ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
    print(1)
else:
    print(0)
