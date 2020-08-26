"""
https://www.hackerrank.com/challenges/equal/problem
Using Greedy Algorithm - Same as Coin Change Problem 
This problem is equivalent to take away the chocolate bar(s) from each chosen one until every one is equal.
Calculate ops for each element divided into 1, 2 and 5 and find minimum sum.
Note that make all has minimum chocolate is not always the correct answer.
There can also be case f(min) > f(min-1), but f(min) < f(min-5) is always right.
So, we should find the minimum value for {f(min), f(min-1), ..., f(min-4)}
"""
def equal(arr):
    m = min(arr)
    ops = [0] * 5

    for j in range(5):
        freq = [0] * len(arr)

        for i, a in enumerate(arr):
            q1, r1 = divmod(a-m+j, 5)
            q2, r2 = divmod(r1, 2)
            freq[i] = q1 + q2 + r2

        ops[j] = sum(freq)

    return min(ops)
