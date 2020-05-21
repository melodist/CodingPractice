"""
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""
def minimumBribes(q):
    ans = 0
    
    first, second, third = 1, 2, 3
    for x in q:
        if x == first:
            first = second
            second = third
            third += 1
        elif x == second:
            ans += 1
            second = third
            third += 1
        elif x == third:
            ans += 2
            third += 1
        else:
            print('Too chaotic')
            return
        
    print(ans)
