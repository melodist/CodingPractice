"""
https://www.hackerrank.com/challenges/waiter/problem
"""
def isprime(target, primes):
    for p in primes:
        if target % p == 0:
            return False
    return True

def waiter(number, q):
    a = number
    primes = [2]
    b = []
    for i in range(q):
        if not a: 
            break
        
        a_temp = []
        b_temp = []
        if i == 0:
            prime = 2
        else:
            prime = primes[-1] + 1
            while not isprime(prime, primes):
                prime += 1
            
        while a:
            x = a.pop()
            if x % prime == 0:
                b_temp.append(x)
            else:
                a_temp.append(x)
        
        a = a_temp
        b += b_temp[::-1]
        primes.append(prime)

    return b + a[::-1]
