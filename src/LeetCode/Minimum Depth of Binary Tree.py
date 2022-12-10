"""
https://leetcode.com/problems/minimum-depth-of-binary-tree
Using BFS
"""
#1. My Solution (509ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = [root]
        depth = 1

        while q:
            next_nodes = []
            for cur in q:
                if cur.left == None and cur.right == None:
                    return depth
                
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            
            depth += 1
            q = next_nodes
