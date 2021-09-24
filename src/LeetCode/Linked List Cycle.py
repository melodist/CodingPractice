"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
Graph Problem
"""
#1. My Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        chaser = head
        if not head or head.next == None or head.next.next == None:
            return False
        runner = head.next.next
        
        while runner != None and runner.next != None:
                if runner == chaser:
                    break
                runner = runner.next.next
                chaser = chaser.next
                
        return True if chaser == runner else False

#2. Other Solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s=f=head
        while f and f.next and f.next.next:
            s=s.next
            f=f.next.next
            if s==f:
                return True
        return False
