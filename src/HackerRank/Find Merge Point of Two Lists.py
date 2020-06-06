"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
Find the length of each list, and move the pointer of longer list by the difference of length.
"""
def findMergeNode(head1, head2):
    len1, len2 = 0, 0

    cur1 = head1
    while cur1:
        len1 += 1
        cur1 = cur1.next

    cur2 = head2
    while cur2:
        len2 += 1
        cur2 = cur2.next

    cur1, cur2 = head1, head2
    if len1 > len2:
        d = len1 - len2
        for i in range(d):
            cur1 = cur1.next
    else:
        d = len2 - len1
        for i in range(d):
            cur2 = cur2.next

    while cur1:
        if cur1 == cur2:
            return cur1.data
        cur1 = cur1.next
        cur2 = cur2.next
