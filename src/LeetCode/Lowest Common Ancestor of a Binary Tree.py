"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
Using postorder traverse
"""
#1. My Solution (82ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root: return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are descendant of root, root is LCA
        if left and right:
            return root

        # If p and q are not descendant of root
        if not left and not right:
            return None

        return left if left else right
    
#2. Other Solution (57ms)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 
        if root == p or root == q: return root 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if left: return left 
        if right: return right 
        return None 
