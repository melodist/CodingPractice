"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
"""
#1. My Solution
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        return stack == stack[::-1]
        
#2. Optimal Solution
# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        
        # Make Reversed List of backward half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
            
        return True
