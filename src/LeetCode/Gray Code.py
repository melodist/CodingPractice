"""
https://leetcode.com/problems/gray-code/
Bitwise Problem
"""
#1. My Solution
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        ans = [0,1]
        
        '''
        grey code can be obtained by adding 1 to all numbers in reverse order ,
        ( need to keep original answer as well)
        0 | 1 -> 00 01 | 11 10 -> 000 001 011 010 | 110 111 101 100 
        
        '''
        for i in range(1,n):
          for ele in ans[::-1]:
            ans.append(ele|(1<<i))

        return ans
