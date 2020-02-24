""" Greedy_Scale
저울추 최소값이 1이 아닐 경우 최소값은 당연히 1  
모든 저울추의 값을 더한 경우 이상의 값은 측정 불가  
누적합[i]+1이 원배열[i+1]보다 커야됨
"""
def solution(weight):
    weight.sort()
    if weight[0] > 1:
        return 1
    
    tmpsum = 0
    for i in range(len(weight)-1):
        tmpsum += weight[i]
        if tmpsum+1 < weight[i+1]:
            return tmpsum + 1

    return tmpsum + weight[-1] + 1
