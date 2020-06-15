"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/627/
Using Mirrored Tree
deque vs Queue : https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque
Queue is intended for allowing different threads to communicate using queued messages/data, 
whereas collections.deque is simply intended as a datastructure. 
"""
#1. Recursive Solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            return(t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)
        
#2. Iterative Solution
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root, root])
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True
