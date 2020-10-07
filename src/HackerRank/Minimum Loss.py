"""
https://www.hackerrank.com/challenges/minimum-loss/problem
"""
#1. My Solution
# Compare only adjacent elements because we want to find minimum
import sys


def minimumLoss(price):
    index = {key:val for val, key in enumerate(price)}
    price_sorted = sorted(price)
    ans = sys.maxsize
    for i in range(1, len(price)):
        # check if bigger element has smaller index
        if index[price_sorted[i-1]] > index[price_sorted[i]]:
            ans = min(ans, price_sorted[i] - price_sorted[i-1])

    return ans
    
#2. Other Solution using binary search
import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node        


    def ceil(self, inp):
        return self._ceil(self.root, inp)

    def _ceil(self, root, inp):  
        # Base Case 
        if root == None: 
            return -1
        
        # We found equal key 
        if root.data == inp : 
            return root.data
        
        # If root's key is smaller, ceil must be in right subtree 
        if root.data < inp: 
            return self._ceil(root.right, inp) 
        
        # Else, either left subtre or root has the ceil value 
        val = self._ceil(root.left, inp) 
        return val if val >= inp else root.data  


def minimumLoss(price):
    tree = BinarySearchTree()
    tree.insert(price[0])
    ans = sys.maxsize
    for p in price[1:]:
        u = tree.ceil(p)
        print(u, p)
        ans = min(ans, u - p) if u > p else ans
        tree.insert(p)

    return ans
