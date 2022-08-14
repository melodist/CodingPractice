"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Using Recursion
"""
#1. My Solution (54ms)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {2: "abc", 
                      3: "def",
                     4: "ghi",
                     5: "jkl",
                     6: "mno", 
                     7: "pqrs",
                     8: "tuv",
                     9: "wxyz"}
        
        ans = []
        
        for i in digits:
            if not ans:
                for c in letter_map[int(i)]:
                    ans.append(c)
            else:
                temp = []
                for c in letter_map[int(i)]:
                    for s in ans:
                        temp.append(s+c)
                ans = temp
                    
        return ans
    
#2. Other Solution (25ms)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        def dfs(i, comb):
            if i >= len(digits):
                res.append("".join(comb))
                return
            
            for char in map[int(digits[i])]:
                comb.append(char)
                dfs(i+1, comb)
                comb.pop()
                    
        dfs(0, [])
        return res if res != [""] else []
