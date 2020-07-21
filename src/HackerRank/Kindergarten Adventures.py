"""
https://www.hackerrank.com/challenges/kindergarten-adventures/problem
"""
#1. Brute Force
def solve(t):
    class Node():
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    n = len(t)
    head = Node(t[0])
    cur = head
    for i in t[1:]:
        cur.next = Node(i)
        cur = cur.next      
    cur.next = head

    cur1 = head
    i = 1
    max_count = 0
    answer = 1
    while i <= n:
        cur2 = cur1
        time = 0
        count = 0
        while cur2.next != cur1:
            if cur2.value <= time:
                count += 1

            cur2 = cur2.next
            time += 1

        if count > max_count:
            max_count = count
            answer = i

        i += 1
        cur1 = cur1.next
            
    return answer

#2. Optimized Solution
def solve(t):
    # Store the count
    n = len(t)
    arr = [0] * (n)
    for j,i in enumerate(t):
        if(i >= n or i == 0 ):
            continue
        arr[(j+1) % n] += 1
        arr[j-i + 1 ] -= 1
        
    maxv = -1
    maxp = 0
    temp = 0
    for j,i in enumerate(arr):
        temp = temp + i
        if(temp > maxv):
            maxv = temp
            maxp = j
            
    return maxp + 1
