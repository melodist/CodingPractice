"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""
def kaprekarNumbers(p, q):
    def digits(n):
        ans = 0
        while n != 0:
            n //= 10
            ans += 1
        return ans
    
    res = []
    for i in range(p, q+1):
        d = digits(i)
        l, r = divmod(i*i, 10**d)
        if l + r == i:
            res.append(i)

    if res:
        print(' '.join(map(str, res)))
    else:
        print('INVALID RANGE')
