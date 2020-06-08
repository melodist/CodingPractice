"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
"""
#1. My Solution
def reverse(head):
    if head == None:
        return head

    front = head
    rear = head.next
    head.next = None

    while rear:
        front.prev = rear
        rear.prev = rear.next
        rear.next = front

        front = rear
        rear = rear.prev
        
    front.prev = None
    return front

#2. Simple Solution
def reverse(head):
    while head.next:
        head.prev, head.next, head = head.next, head.prev, head.next
    head.prev, head.next = None, head.prev
    return head
