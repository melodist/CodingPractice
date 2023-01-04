"""
만나는 지점과 순환 기점 사이의 거리 m
처음 만날 때 slow가 k만큼 이동하면 만나는 지점의 head로부터의 거리는 k-m
순환 사이클의 길이를 l이라 하면 l = k
따라서 처음 만난 지점에서 k-m만큼 이동하면 순환 기점에 도달
처음 만난 이후 한 포인터를 head로 되돌리고 k-m의 속도로 이동하면 서로 다시 만남
다시 만나는 지점이 순환 기점
"""
#1. My Solution (96ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # No Cycle
        if head == None or head.next == None: return None

        fast = head.next.next
        slow = head.next
        pos = 0

        while fast != slow:
            if fast == None:
                return None

            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None

        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
