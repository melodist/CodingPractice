"""
https://www.hackerrank.com/challenges/morgan-and-a-string/problem
Using suffix array
"""
#1. Optimal Solution
def morgan(a, b):
    a += 'z'
    b += 'z'

    for _ in range(len(a) + len(b) - 2):
        if a < b:  # Python compares strings in lexicographical order
            yield a[0]
            a = a[1:]
        else:
            yield b[0]
            b = b[1:]

def morganAndString(a, b):
    return ''.join(morgan(a, b))
    
#2. Solution using suffix array (Timeout in Python 3 and Pypy3)
def morganAndString(a, b):
    answer = ''
    s = a + 'a' + b + 'a'
    N = len(s)

    equivalence = {t:i for i, t in enumerate(sorted(set(s)))}
    cls = [equivalence[t] for t in s]

    ns = [(2**i) % N for i in range(int(math.ceil(math.log(N,2))))]

    for n in ns[:-1]:
        result = sorted(zip(cls, cls[n:]+cls[:n], range(N)))
        result0, result1, inds = list(zip(*result))

        cls[inds[0]] = 0
        for j in range(1, N):
            cls[inds[j]] = cls[inds[j-1]]
            if (result0[j], result1[j]) != (result0[j-1], result1[j-1]):
                cls[inds[j]] += 1
    n = ns[-1]
    result = sorted(zip(cls, cls[n:]+cls[:n], range(N)))

    dic = {z[2]:z[0] for z in result}
    
    size_a, size_b = len(a), len(b)
    pos1, pos2 = 0, size_a + 1
    while True:
        if pos1 > size_a - 1 and pos2 > size_a + size_b:
            break
        if pos1 > size_a - 1:
            answer += s[pos2]
            pos2 += 1
            continue
        if pos2 > size_a + size_b:
            answer += s[pos1]
            pos1 += 1
            continue

        if dic[pos1] < dic[pos2]:
            answer += s[pos1]
            pos1 += 1
        else:
            answer += s[pos2]
            pos2 += 1

    return answer
