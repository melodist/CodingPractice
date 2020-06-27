"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
"""
#1. My Solution
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nodes = []
        levels = []
        q = deque([(root, 1)])
        
        while q:
            cur, height = q.popleft()
            nodes.append(cur.val)
            levels.append(height)
            for node in (cur.left, cur.right):
                if node:
                    q.append((node, height + 1))
        ans = []
        temp = []
        prev = 1
        for n, h in zip(nodes, levels):
            if h != prev:
                ans.append(temp)
                temp = [n]
                prev = h
            else:
                temp.append(n)
                
        ans.append(temp)
        return ans
        
#2. Optimal Solution
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 1)])
        ans = []
        temp = []
        level = 1
        while q:
            cur, height = q.popleft()
            if height != level:
                ans.append(temp)
                temp = []
                level = height
                
            temp.append(cur.val)
            
            if cur.left:
                q.append((cur.left, height + 1))            
            if cur.right:
                q.append((cur.right, height + 1))
                
        ans.append(temp)
        
        return ans
        
#3. Recursive Solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(n, res, level):
            if not n: return []
            if level == len(res):
                res.append([])
            res[level].append(n.val)
            if n.left: res = traverse(n.left, res, level+1)
            if n.right: res = traverse(n.right, res, level+1)
                
            return res

        return traverse(root, [], 0)
