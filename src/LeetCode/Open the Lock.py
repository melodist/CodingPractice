"""
https://leetcode.com/problems/open-the-lock
Using BFS
"""
#1. My Solution (918ms)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus_one(s, i):
            arr = list(s)
            if s[i] == '9':
                arr[i] = '0'
            else:
                arr[i] = str(int(s[i]) + 1)
            
            return ''.join(arr)

        def minus_one(s, i):
            arr = list(s)
            if s[i] == '0':
                arr[i] = '9'
            else:
                arr[i] = str(int(s[i]) - 1)
            
            return ''.join(arr)

        def bfs(target, deadends):
            q = deque([['0000', 0]])
            visited = set()
            deadends = set(deadends)

            while q:
                temp = []
                for s, cnt in q:
                    if s == target:
                        return cnt

                    if s in deadends or s in visited:
                        continue

                    for i in range(4):
                        temp.append([plus_one(s, i), cnt+1])
                        temp.append([minus_one(s, i), cnt+1])

                    visited.add(s)


                q = temp

            return -1

        return bfs(target, deadends)
    
#2. Other Solution (110ms)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target == '0000': return 0
        if "0000" in deadends:
            return -1
        deadends.add("0000")
        deadends.add(target)
        
        nbr = {str(i): [str((i - 1) % 10), str((i + 1) % 10)] for i in range(10)}
        start, end = {"0000"}, {target}
        count = 0
        while start and end:
            count += 1
            if len(start) > len(end):
                start, end = end, start
            tmp = set()
            for wheels in start:
                for i in range(4):
                    for num in nbr[wheels[i]]:
                        nxt = wheels[:i] + num + wheels[i + 1:]
                        if nxt in end:
                            return count
                        if nxt not in deadends:
                            deadends.add(nxt)
                            tmp.add(nxt)
            start = tmp
        return -1
