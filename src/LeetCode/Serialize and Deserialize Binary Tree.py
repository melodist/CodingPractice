"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
Binary Tree Problem
"""
#1. Solution using preorder traverse (838ms)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self.serialize_preorder(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        global node_list
        node_list = data.split(',')
        return self.deserialize_preorder()
        
    def serialize_preorder(self, root):
        return [str(root.val)] + self.serialize_preorder(root.left) + self.serialize_preorder(root.right) if root else ['#']

    def deserialize_preorder(self):
        global node_list
        first = node_list[0]
        node_list = node_list[1:]
        if first == '#': return None
        root = TreeNode(int(first))
        
        root.left = self.deserialize_preorder()
        root.right = self.deserialize_preorder()

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

#2. Other Solution (107ms)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    # We will use N for null in the encode
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
         
        # travel the tree by levels
        result = []
        queue = deque([root])
        while queue:
            num_of_items = len(queue)
            
            for i in range(num_of_items):
                current = queue.popleft()
                if not current:
                    result.append("N")
                else:
                    result.append(str(current.val))
                    queue.append(current.left)
                    queue.append(current.right)
        return ",".join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_arr = data.split(",")
        if not data or not data_arr:
            return None

        root = TreeNode(int(data_arr[0]))
        queue = deque([root])
        for i in range(1, len(data_arr), 2):
            current = queue.popleft()

            # construct left, right child then make them to be child of current
            if data_arr[i] != "N":
                left_child = TreeNode(int(data_arr[i]))
                current.left = left_child
                queue.append(left_child)

            if data_arr[i + 1] != "N":
                right_child = TreeNode(int(data_arr[i + 1]))
                current.right = right_child
                queue.append(right_child)

        return root
