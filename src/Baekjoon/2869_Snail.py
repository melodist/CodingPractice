"""
2869번: 달팽이는 올라가고 싶다
https://www.acmicpc.net/problem/2869

달팽이가 나무 올라가는데 n일 걸린다고 가정하면
a * n - b * (n-1) >= v

탐색 완료 조건 : mid는 조건 만족, mid-1은 조건 불만족
"""
def snail(a, b, v):
    start = 0
    end = 10**9
    
    while start <= end:
        mid = (start+end) // 2

        if (a-b) * (mid-1) + a >= v:
            if (a-b) * (mid-2) + a < v:
                print(mid)
                break
            else:
                end = mid-1
        else:
            start = mid+1

a, b, v = map(int, input().split())
snail(a, b, v)
