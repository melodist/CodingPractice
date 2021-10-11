"""

Find tree height
"""
#1. My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(u):
            dist = 0
            q = deque([(u, 0)])
            visited = set()
            visited.add(u)
            
            while q:
                u, d = q.popleft()
                dist = max(dist, d)
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, d+1)) 
                        
            return dist
        
        q = deque([(root, 0)])
        graph = defaultdict(list)
        dist_max = 0
        dist = {}
                
        while q:
            curr, d = q.popleft()
            dist[curr] = d
            dist_max = max(d, dist_max)
            
            if curr.left:
                graph[curr].append(curr.left)
                graph[curr.left].append(curr)
                q.append((curr.left, d+1))
            if curr.right:
                graph[curr].append(curr.right)
                graph[curr.right].append(curr)
                q.append((curr.right, d+1))

        answer = 0
        
        # find max
        for k in dist:
            if dist[k] == dist_max:
                answer = max(answer, bfs(k))
          
        return answer

#2. Other Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia = 0
        
        def height(root):
            if not root: 
                return 0
            left, right = height(root.left), height(root.right)
            self.dia = max(self.dia, left + right)
            return 1 + max(left, right)
            
        height(root)
        return self.dia
