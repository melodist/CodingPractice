"""
https://leetcode.com/problems/add-two-numbers/submissions/
Using Linked List
"""
#1. My Solution (139ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        carry = 0
        while (l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            carry, mod = divmod(v1+v2+carry, 10)
            result.append(mod)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        node_head = ListNode(result[0])
        node_prev = node_head
        for i in result[1:]:
            node_next = ListNode(i)
            node_prev.next = node_next
            node_prev = node_next
            
        if carry:
            node_next = ListNode(carry)
            node_prev.next = node_next
            
        return node_head
            

#2. Other Solution (56ms)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode(0)
        root=head
        
        carry=0
        
        while l1 or l2 or carry:
            val1=(l1.val if l1 else 0)
            val2=(l2.val if l2 else 0)
            carry, out=divmod(val1+val2+carry,10)
            
            root.next=ListNode(out)
            root=root.next
            
            l1=(l1.next if l1 else None)
            l2=(l2.next if l2 else None)  
            
        return head.next
