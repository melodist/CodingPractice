"""
https://leetcode.com/problems/increasing-order-search-tree/
Using Binary Search Tree
"""
#1. My Solution (39ms, 13.8MB)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root;
        
        if root.right:
            root.right = self.increasingBST(root.right)
        
        if root.left:
            prev = root.left
            if prev.right:
                prev.right = self.increasingBST(prev.right)
                end_node = self.find_right_edge(prev.right)
                end_node.right = root
            else:
                prev.right = root
            root.left = None
            return self.increasingBST(prev)
        else:
            return root
        
    def find_right_edge(self, root: TreeNode):
        if not root.right:
            return root
        else:
            return self.find_right_edge(root.right)
        
#2. Other Solution(33ms, 13.9MB)
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
