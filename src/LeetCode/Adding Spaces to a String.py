"""
https://leetcode.com/contest/weekly-contest-272/problems/adding-spaces-to-a-string/
String Problem
"""
#1. My Solution (838ms)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = s[:spaces[0]]
        spaces += [len(s)]
        for i in range(1, len(spaces)):
            answer += " " + s[spaces[i-1]:spaces[i]]
        
        return answer
    
#2. Other Solution (604ms)
def split_string(string: str, split_indices: list[int]) -> Iterable[str]:
    curr_idx = 0
    for split_idx in split_indices:
        yield string[curr_idx:split_idx]
        curr_idx = split_idx
    yield string[curr_idx:]

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return " ".join(split_string(s, spaces))

