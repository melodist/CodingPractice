"""
https://leetcode.com/problems/longest-common-prefix/
Binary Search 이용.
string도 array라는 것을 적극 활용할 것.
"""
class Solution:
    def check(self, mid, strs):
        for i in range(1, len(strs)):
            if strs[0][:mid] != strs[i][:mid]:
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
    
        prefix = strs[0]
        start, end = 1, len(prefix)
        
        while start<=end:
            mid = int((start+end) / 2)
            if self.check(mid, strs):
                print(prefix[:mid])
                start = mid + 1
            else:        
                end = mid - 1
        return prefix[:int((start+end)/2)]
