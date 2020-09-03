"""
https://www.hackerrank.com/challenges/special-palindrome-again/problem
1. Compress string using count (ex. abcaaa -> a1 b1 c1 a3)
2. Find number of substrings that has same characters (ex. aaaa)
3. Find number of substrings that has one different character in middle (ex. aabaa)
"""
def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
    
    print(l)
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans
