"""
https://leetcode.com/problems/path-sum/
Using DFS
"""
#1. My Solution (31ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        stack = []
        stack.append((0, root))
        
        while stack:
            s, node = stack.pop()

            if not node.left and not node.right:
                if targetSum == s + node.val:
                    return True
            
            if node.left:
                stack.append((s + node.val, node.left))
                
            if node.right:
                stack.append((s + node.val, node.right))
            
                
        return False
