"""
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#1. My Solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        def insert(left, right):
            if right - left == 1:
                return TreeNode(nums[right], TreeNode(nums[left]))
            elif right == left:
                return TreeNode(nums[right])
            mid = (left + right) // 2
            return TreeNode(nums[mid], insert(left, mid-1), insert(mid+1, right))
            
        return insert(0, len(nums)-1)
        
#2. Other Solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def preorder(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = preorder(left, mid - 1)
            root.right = preorder(mid + 1, right)
            return root
        
        return preorder(0, len(nums) - 1)
