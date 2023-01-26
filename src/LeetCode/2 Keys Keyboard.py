"""
https://leetcode.com/problems/2-keys-keyboard
Using Dynamic Programming
"""
#1. My Solution (776ms)
class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def helper(screen, clipboard):
            if (screen, clipboard) in cache: return cache[(screen, clipboard)]
            if screen == n: return 0
            if screen > n: return float("Inf")
            
            copy_paste = helper(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = helper(screen + clipboard, clipboard) + 1

            cache[(screen, clipboard)] = min(copy_paste, paste)    
            return cache[(screen, clipboard)]
        
        return helper(1, 0)
    
#2. Other Solution (37ms)
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i*i<=n:
            if n%i == 0: 
                ans+=i
                n/=i
            else:
                i+=1
        if n!=1:
            ans+=n

        return(int(ans))
