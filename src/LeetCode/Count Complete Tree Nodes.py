"""
https://leetcode.com/problems/count-complete-tree-nodes/description/
Count Perfect Binary Tree + Count Normal Binary Tree
"""
#1. My Solution (85ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        hl = hr = 0
        l = r = root

        while l != None:
            l = l.left
            hl += 1
            

        while r != None:
            r = r.right
            hr += 1
            
        return 2 ** hl - 1 if hl == hr else 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
        
