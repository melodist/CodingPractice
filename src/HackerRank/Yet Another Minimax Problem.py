"""
https://www.hackerrank.com/challenges/yet-another-minimax-problem/
Bit 개수가 가장 많은 수와 그 이외의 수들로 나누고 두 집합 간의 XOR 값만을 비교한다.
모든 수의 Bit 개수가 같을 경우 비교 기준의 Bit 개수를 1개 줄인다.
"""
import math

def find_minimum(base, case, nons):
    mini = 2**(base+1) - 1
    for non in nons:
        temp = case ^ non
        if temp < mini:
            mini = temp
            
    return mini

def divide_list(base, a):
    cases = []
    nons = []
    mask = 1 << base
    print(mask)
    for num in a:
        if num & mask == mask:
            cases.append(num)
        else:
            nons.append(num)
    
    return cases, nons

# Complete the anotherMinimaxProblem function below.
def Minimax(base, list_one, list_zero):
    if base < 0: return 0
    answer = []
    if list_one and list_zero:
        for case in list_one:
            answer.append(find_minimum(base, case, list_zero)) 
        return min(answer)
    elif not list_one:
        return Minimax(base, list_zero, [])
    else:
        list2_one, list2_zero = divide_list(base-1, list_one)
        return Minimax(base-1, list2_one, list2_zero)
        
def anotherMinimaxProblem(a):
    p = max(a)
    if p == 0:
        return 0
        
    a = list(set(a))
    if len(a) == 1: return 0
    
    base = math.floor(math.log(p, 2))
    list_one, list_zero = divide_list(base, a)

    return Minimax(base, list_one, list_zero)
