"""
https://programmers.co.kr/learn/courses/30/lessons/42892/
"""
#1. My Solution
import sys


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        cur = self.root
        parent = None
        while cur:
            parent = cur
            if cur.x < node.x:
                cur = cur.right
            else:
                cur = cur.left

        if parent.x < node.x:
            parent.right = node
        else:
            parent.left = node


    def preorder(self):
        stack = [self.root]
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return ans

    def postorder(self, node):
        if node:
            return self.postorder(node.left) + self.postorder(node.right) + [node.val]
        else:
            return []
            
    def postorder_nonrecursive(self):
        stack = [self.root]
        visited = set()
        answer = []
        
        while stack:
            currNode = stack[-1]
            if currNode.left and currNode.left.val not in visited:
                stack.append(currNode.left)
            else:
                if currNode.right and currNode.right.val not in visited:
                    stack.append(currNode.right)
                else:
                    answer.append(currNode.val)
                    visited.add(currNode.val)
                    stack.pop()
                
        return answer

class Node():
    def __init__(self, node):
        self.val = node[0]
        self.x = node[1]
        self.y = node[2]
        self.left = None
        self.right = None


def solution(nodeinfo):
    sys.setrecursionlimit(2000)
    nodes = [()] * len(nodeinfo)
    tree = Tree()

    for i, (x, y) in enumerate(nodeinfo):
        nodes[i] = (i+1, x, y)
    nodes.sort(key=lambda x: (-x[2], x[1]))

    for node in nodes:
        tree.insert(Node(node))

    return [tree.preorder(), tree.postorder(tree.root)]
