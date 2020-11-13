"""
https://www.hackerrank.com/challenges/pylons/problem
Using two pointers
"""
#1. My Solution
def pylons(k, arr):
    n = len(arr)
    i,j,trans,flag,loc=0,0,0,0,0
    while(i<n):
        trans+=1
        j=i+k-1
        
        if(j>n):
            j=n-1
            
        while (loc<=j<n and arr[j]==0):
            j-=1
            
        if(j<loc):
            return -1
        else:
            loc=j+1
            j+=k
            i=j
            
    return trans
