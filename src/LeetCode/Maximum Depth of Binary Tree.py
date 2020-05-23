"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
