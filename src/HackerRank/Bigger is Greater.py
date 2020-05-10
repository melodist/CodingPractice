"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""
def biggerIsGreater(w):
    front = -1
    w = list(w)
    n = len(w)
    for i in range(n-1):
        if ord(w[i]) < ord(w[i+1]):
            front = i
    
    if front == -1: return 'no answer'
  
    # front 뒤의 영역은 내림차순으로 정리되어 있기 때문에
    # front보다 큰 값 중 가장 마지막에 나오는 값이 front보다 큰 값 중 가장 작은 값이 된다.
    rear = -1
    for i in range(front + 1, n):
        if ord(w[front]) < ord(w[i]):
            rear = i
    
    w[front], w[rear] = w[rear], w[front]
    bigger = w[front+1:]
    bigger.sort()
    
    w[front+1:] = bigger
    
    return ''.join(w)
