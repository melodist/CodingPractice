"""
https://leetcode.com/problems/minimum-window-substring/description/
Using Sliding Window
"""
#1. My Solution (167ms)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = Counter()
        t_count = Counter(t)
        
        left = right = valid = start = 0
        ans_size = float('inf')
        while right < len(s):
            # put right char
            c = s[right]

            # move window right
            right += 1

            s_count[c] += 1
            if s_count[c] == t_count[c]:
                valid += 1


            # check if left could be popped
            while valid == len(t_count):
                if right - left < ans_size:
                    start = left
                    ans_size = right - left

                d = s[left]
                # move window left
                left += 1

                if s_count[d] == t_count[d]:
                    valid -= 1
                s_count[d] -= 1

        return s[start:start+ans_size] if ans_size != float('inf') else ""
      
#2. Other Solution (87ms)
class Solution(object):
    def minWindow(self, s, t):
        
        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1
        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0
        
        for current_end, ch in enumerate(s, 1):
            if target_count_dict[ch] > 0:
                remain_missing -= 1
            target_count_dict[ch] -= 1
            
            if remain_missing == 0:
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end
                
                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1
        
        return s[start_pos:end_pos] if end_pos != float('inf') else ""
