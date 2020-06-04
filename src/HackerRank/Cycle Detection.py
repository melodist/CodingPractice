"""
https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
Use two pointers.
If two pointers refer to same node, list has a cycle.
"""
def has_cycle(head):
    fast = head
    slow = head
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return 1
    return 0
