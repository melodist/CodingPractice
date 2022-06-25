"""

Using Recursion
"""
#1. My Solution (42ms)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        arr = [0] * (rowIndex + 1)
        arr_prev = self.getRow(rowIndex-1)
        for i in range(rowIndex):
            arr[i] += arr_prev[i]
        for i in range(rowIndex):
            arr[i+1] += arr_prev[i]
            
        return arr
        
#2. Other Solution (26ms)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # length of row will be 1 more than the rowIndex
        row = [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            # we started from 1st index till 2nd last index of row beacuse 1st and last element will always be zero in any row
            for j in range(i,0,-1):
                # we will move from last and keep updating the row indices
                # the reason why it go backforward for the second j loop, is that if we go forward, the i th element will be changed by the i-1 th element. And it will influence the next element's calculation
                row[j] = row[j] + row[j-1]
        return row
