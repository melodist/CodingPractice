"""
https://leetcode.com/problems/house-robber-iii
Using Dynamic Programming
"""
#1. My Solution (64ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = dict()
        def dp(node, robbed):
            if not node:
                return 0

            if (node, robbed) in memo:
                return memo[(node, robbed)]

            if robbed:
                res = node.val + dp(node.left, False) + dp(node.right, False)
            else:
                res = max(dp(node.right, True), dp(node.right, False)) \ # caution for line breaks
                + max(dp(node.left, True), dp(node.left, False))  

            memo[(node, robbed)] = res

            return res

        return max(dp(root, True), dp(root, False))
