"""
https://leetcode.com/problems/reduce-array-size-to-the-half/

"""
#1. My Solution (1186ms)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_dict = defaultdict(int)
        n = len(arr)
        
        for i in arr:
            freq_dict[i] += 1
            
        freq = sorted(freq_dict.items(), key=lambda x: -x[1])
        deleted = 0
        ans = 1
        for k, v in freq:
            deleted += v
            if deleted >= n / 2:
                return ans
            ans += 1
        
        return -1
    
#2. Other Solution (603ms)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
        num_freq = sorted(cnt.values(), reverse=True)  # Sort dictionary by their frequency (descending order)
        
        half_size = len(arr) // 2
        ans = 0
        
        while half_size > 0:
            half_size -= num_freq[ans]
            ans += 1
        
        return ans
