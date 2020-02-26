# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(None, head)
        
    def reverse(self, prev, current):
        if current is not None:
            next = current.next
            current.next = prev
            return self.reverse(current, next)
        else:
            return prev
        
