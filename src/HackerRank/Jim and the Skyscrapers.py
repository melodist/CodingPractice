"""
https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem
"""
#1. My Solution
def solve(arr):
    stack = []
    answer = 0
    for a in arr:
        while stack and a > stack[-1][0]:
            stack.pop()

        if stack and a == stack[-1][0]:
            answer += stack[-1][1] * 2
            stack[-1][1] += 1
        else:
            stack.append([a, 1])

    return answer
    
#2. Other Solution
def query(T, n, L, R, i, j):
  if R < i or j < L: return -1
  if i <= L and R <= j: return T[n]
  return max(query(T, n * 2, L, (L + R) // 2, i, j), query(T, n * 2 + 1, (L + R) // 2 + 1, R, i, j))
  
def build(T, n, L, R):
  if L == R:
    T[n] = arr[L]
  else:
    build(T, n * 2, L, (L + R) // 2)
    build(T, n * 2 + 1, (L + R) // 2 + 1, R)
    T[n] = max(T[n * 2], T[n * 2 + 1])
    
def rmq(T, i, j, N): 
  return query(T, 1, 0, N - 1, i, j)

def solve(arr):
    MAX_N = 10**5
    N = len(arr)
    T = [0] * 4 * MAX_N
    last = [0] * 10 * MAX_N
    C = [0] * 10 * MAX_N

    build(T, 1, 0, N - 1)
    res = 0
    for i in range(N):
        if last[arr[i]] == -1 or rmq(T, last[arr[i]], i, N) > arr[i]:
            C[arr[i]] = 0
        
        res += C[arr[i]]
        C[arr[i]] += 1
        last[arr[i]] = i

    return res * 2

    return res * 2
