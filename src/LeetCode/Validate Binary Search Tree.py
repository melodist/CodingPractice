"""
https://leetcode.com/problems/validate-binary-search-tree
"""
#1. My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left = self.maxmin(root.left)[0] if root.left else root.val - 1
        right = self.maxmin(root.right)[1] if root.right else root.val + 1
        
        if left < root.val < right:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
        
    def maxmin(self, root):
        q = deque([root])
        a1 = -10E10
        a2 = 10E10
        while q:
            cur = q.popleft()
            a1 = max(a1, cur.val)
            a2 = min(a2, cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            
        return a1, a2
        
#2. Inorder Traverse
from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = deque([]), float('-inf')
        
        while stack or root:
            # Go to left end of BST
            while root:
                stack.append(root)
                root = root.left
            # Inorder Traverse (This is not BFS)
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
            
        return True
    
#3. Solution using recursion (46ms)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidTree(root, min_node, max_node):
            if not root: return True
            if min_node and root.val <= min_node.val: return False
            if max_node and root.val >= max_node.val: return False

            return isValidTree(root.left, min_node, root) and isValidTree(root.right, root, max_node)

        return isValidTree(root, None, None)
