"""
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
"""
#1. Stack
def reversePrint(head):
    stack = []
    while head:
        stack.append(head.data)
        head = head.next

    while stack:
        print(stack.pop())
        
#2. Recursive
def reversePrint(head):
    if not head:
        return
    reversePrint(head.next)
    print(head.data)
