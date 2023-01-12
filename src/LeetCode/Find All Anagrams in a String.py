"""
https://leetcode.com/problems/find-all-anagrams-in-a-string
Using Sliding Window
"""
#1. My Solution (165ms)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        need = Counter(p)
        window = Counter()

        left = right = valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            
            window[c] += 1
            if need[c] == window[c]:
                valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    answer.append(left)

                d = s[left]
                left += 1

                if need[d] == window[d]:
                    valid -= 1
                window[d] -= 1

        return answer
