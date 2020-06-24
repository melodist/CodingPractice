"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            temp = [1] * i
            for j in range(1, i-1):
                temp[j] = ans[-1][j] + ans[-1][j-1]
            ans.append(temp)
            
        return ans
