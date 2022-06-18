"""
https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
Using Recursion
"""
#1. My Solution (45ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        curr = head.next
        head.next = self.swapPairs(head.next.next)
        curr.next = head
        
        return curr
    
#2. Non-recursive solution (19ms)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        prev, curr = dummy, head

        while curr and curr.next:

            #Define the next two adjacent nodes
            second = curr.next
            nextPair = curr.next.next


            second.next = curr
            curr.next = nextPair
            prev.next = second

            #Update the pointers

            prev = curr
            curr = nextPair
        return dummy.next
