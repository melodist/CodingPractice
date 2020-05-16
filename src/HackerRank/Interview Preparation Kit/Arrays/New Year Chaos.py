"""
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""
#1. Brute Force O(n^2)
def minimumBribes(q):
    ans = 0
    for i in range(len(q)):
        if q[i] - i > 2: 
            print('Too chaotic')
            return
        
        moves = 0
        for j in range(i + 1, len(q)):
            if q[i] > q[j]:
                moves += 1

        ans += moves
        
    print(ans)

#2. Linear Time Approach O(n)
def minimumBribes(q):
    ans = 0
    
    first, second, third = 1, 2, 3
    for x in q:
        if x == first:
            first = second
            second = third
        elif x == second:
            ans += 1
            second = third
        elif x == third:
            ans += 2
        else:
            print('Too chaotic')
            return          
        third += 1
        
    print(ans)        
