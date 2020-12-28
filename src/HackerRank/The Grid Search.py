"""
https://www.hackerrank.com/challenges/the-grid-search/problem
Implementation Problem
"""
#1. My Solution
def gridSearch(G, P):
    def valid(y, x):
        for i in range(r):
            for j in range(c):
                if G[y+i][x+j] != P[i][j]:
                    return False
                
        return True
    
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    p = []
    for i in range(R-r+1):
        for j in range(C-c+1):
            if G[i][j] == P[0][0]:
                p.append((i, j))
                
    for y, x in p:
        if valid(y, x):
            return 'YES'

    return 'NO'
    
