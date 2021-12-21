"""
https://leetcode.com/problems/finding-3-digit-even-numbers/
Implementation Problem
"""
#1. My Solution (192ms)
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        c = Counter([str(i) for i in digits])
        for i in range(100, 1000):
            if i % 2 == 1:
                continue
                
            flag = True
            d = Counter(list(str(i)))
            
            for j in range(10):
                s = str(j)
                if c[s] < d[s]:
                    flag = False
                    break
                    
            if flag:
                answer.append(i)
                
        return answer

#2. Other Solution (53ms)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = defaultdict(int)
        for digit in digits:
            count[digit] += 1
        r = []
        even_digits = [digit for digit in count if digit % 2 == 0]
        for even_digit in even_digits:
            count[even_digit] -= 1
            for digit1 in count:
                if count[digit1] > 0:
                    count[digit1] -= 1
                    for digit2 in count:
                        if count[digit2] > 0:
                            num = 100 * digit1 + 10 * digit2 + even_digit
                            if num >= 100:
                                r.append(num)
                    count[digit1] += 1
            count[even_digit] += 1
        return sorted(r)
