"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
"""
#1. My Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            cur1, cur2 = l1.next, l2
        else:
            head = l2
            cur1, cur2 = l1, l2.next
        cur = head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
                
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
            
        return head
        
#2. Recursive Solution
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

    if l1 is None: return l2
    elif l2 is None: return l1

    elif l1.val<=l2.val:
        l1.next=self.mergeTwoLists(l1.next,l2)
        return l1

    else:
        l2.next=self.mergeTwoLists(l1,l2.next)
        return l2
