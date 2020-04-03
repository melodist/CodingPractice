"""
https://leetcode.com/problems/balanced-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.find_height(root.left), self.find_height(root.right))
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isBalanced(root.left) and \
                self.isBalanced(root.right) and \
                abs(self.find_height(root.left) - self.find_height(root.right)) <= 1
