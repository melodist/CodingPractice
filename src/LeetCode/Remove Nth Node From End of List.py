# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyhead = ListNode(None)
        dummyhead.next = head
        
        fast = head
        for i in range(n-1):
            fast = fast.next
        
        slow = dummyhead
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummyhead.next
