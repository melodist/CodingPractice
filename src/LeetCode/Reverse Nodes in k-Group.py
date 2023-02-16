"""
https://leetcode.com/problems/reverse-nodes-in-k-group
Using recursion
"""
#1. My Solution (52ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(a, b):
            pre = None
            cur = nxt = a
            while cur != b:
                nxt = cur.next

                # reverse node
                cur.next = pre

                # update pointer
                pre = cur
                cur = nxt

            return pre

        if not head:
            return None
        
        a = b = head
        for i in range(k):
            if not b:
                return head
            b = b.next

        new_head = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
