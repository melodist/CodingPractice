"""
https://www.hackerrank.com/challenges/truck-tour/problem
Using Circular Permutation
"""
def truckTour(petrolpumps):
    n = len(petrolpumps)
    
    for i in range(n):
        truck, passed = 0, 0
        for j in range(n):
            p, d = petrolpumps[(i+j)%n]
            truck += p - d
            if truck < 0:
                break
            passed += 1
        
        if passed == n:
            return i
