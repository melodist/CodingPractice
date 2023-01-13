"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
Using Sliding Window
"""
#1. My Solution (87ms)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = answer = 0
        window = Counter()

        while right < len(s):
            c = s[right]
            right += 1

            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1

                window[d] -= 1

            answer = max(answer, right - left)

        return answer
