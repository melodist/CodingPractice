"""
https://www.hackerrank.com/challenges/lilys-homework/problem
Using sort and map
"""
#1. My Solution
def lilysHomework(arr):
    def solution(a):
        arr = a[:]  # Copy array because this function modifies array
        m = {}
        for i, x in enumerate(arr):
            m[x] = i 
            
        sorted_a = sorted(arr)
        ret = 0
        
        for i in range(len(arr)):
            if arr[i] != sorted_a[i]:
                ret +=1
                
                ind_to_swap = m[sorted_a[i]]
                m[arr[i]] = m[sorted_a[i]]
                arr[i],arr[ind_to_swap] = sorted_a[i],arr[i]

        return ret

    return min(solution(arr), solution(arr[::-1]))
