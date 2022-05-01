"""
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
Using Hash
"""
#1. My Solution
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        selected = {}
        answer = float('inf')
        for i, v in enumerate(cards):
            if v in selected:
                answer = min(answer, i - selected[v] + 1)
            selected[v] = i
                
        return answer if answer < float('inf') else -1
    
#2. Other Solution
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = math.inf
        n = len(cards)
        pos = defaultdict(lambda: -1)
        for i in range(n):
            if pos[cards[i]] != -1:
                ans = min(i - pos[cards[i]] + 1, ans)
            pos[cards[i]] = i
        return ans if ans != math.inf else -1
