"""
https://leetcode.com/problems/letter-case-permutation/
"""
#1. My Solution
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for c in S:
            if c.isalpha():
                temp = ans[:]
                for i in range(len(ans)):
                    ans[i] += c.upper()
                    temp[i] += c.lower()                    
                ans += temp
            else:
                for i in range(len(ans)):
                    ans[i] += c
                    
        return ans

#2. Solution using product
from itertools import product


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        pools = []
        for i in S:
            if i.isalpha():
                pools.append([i, i.swapcase()])
            else:
                pools.append([i])
        ans = []
        for j in product(*pools):
            ans.append(''.join(j))
        return ans
