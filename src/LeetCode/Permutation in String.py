"""
https://leetcode.com/problems/permutation-in-string
Using Sliding Window
"""
#1. My Solution (100ms)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        
        left = right = valid = 0
        
        while right < len(s2):
            c = s2[right]
            right += 1

            # update window
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # find if left moves
            while right - left >= len(s1):

                # find if valid
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1

                # update window
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return False
