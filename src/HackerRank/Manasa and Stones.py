"""
https://www.hackerrank.com/challenges/manasa-and-stones/problem
마지막 값만 확인하면 되므로 a > b일 경우 0*a + (n-1)*b부터 (n-1)*a + 0*b까지 순서대로 추가
"""
def stones(n, a, b):
    ans = []
    if a == b: return [(n-1) * a]
    elif a < b: 
        a, b = b, a
    for i in range(n):
        ans.append(i*a + (n-1-i)*b)
    return ans
