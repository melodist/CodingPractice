"""
"""
#1. Solution Using Linked List
# use linked list
class Solver:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


def solution(n, k, cmd):
    arr = [1] * n
    stack = []

    # initialize linked list
    prev = Solver(0, None, None)
    for i in range(1, n):
        temp = Solver(i, prev, None)
        prev.next = temp
        prev = temp

    cur = prev
    for j in range(n-k-1):
        cur = cur.prev

    for c in cmd:
        if c[0] == 'C':
            arr[cur.val] = 0
            stack.append(cur)

            # connect
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev

            # move cursor
            if cur.next is None:
                cur = cur.prev
            else:
                cur = cur.next

        elif c[0] == 'Z':
            res = stack.pop()
            arr[res.val] = 1
            if res.prev:
                res.prev.next = res
            if res.next:
                res.next.prev = res
        else:
            count = int(c[2:])
            for i in range(count):
                cur = cur.prev if c[0] == 'U' else cur.next

    return ''.join(['O' if x else 'X' for x in arr])

#2. Solution Using Segment Tree
# make segment tree that interval stores sum of not deleted rows
def solution(n, k, cmd):
    # Initialize tree
    def init(start, end, node):
        if start == end:
            tree[node] = 1
        else:
            mid = (start + end) // 2
            tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
        return tree[node]

    def update(start, end, ind, target, value):
        if start > target or end < target:
            return

        tree[ind] += value
        if start == end:
            return

        mid = (start + end) // 2
        update(start, mid, ind * 2, target, value)
        update(mid + 1, end, ind * 2 + 1, target, value)

    # find index for target
    def find(start, end, target, node):
        mid = (start + end) // 2
        if mid == target:
            return tree[node]
        elif mid < target:
            return find(start, mid, target, node * 2)
        else:
            return find(mid + 1, start, target, node * 2 + 1)

    # find sum of intervals
    def find_sum(start, end, ind, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return tree[ind]
        mid = (start + end) // 2
        return find_sum(start, mid, ind * 2, left, right) \
               + find_sum(mid + 1, end, ind * 2 + 1, left, right)

    # find nearest index for target
    def find_left(ind, target):
        sum_target = find_sum(0, n - 1, 1, 0, ind) - target
        left = 0
        right = ind - 1
        while left <= right:
            mid = (left + right) // 2
            value = find_sum(0, n - 1, 1, 0, mid)
            if sum_target <= value:
                # Move left
                ans = mid
                right = mid - 1
            else:
                # Move right
                left = mid + 1

        return mid

    def find_right(ind, target):
        sum_target = find_sum(0, n - 1, 1, 0, ind) + target
        left = ind + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            value = find_sum(0, n - 1, 1, 0, mid)
            if sum_target <= value:
                # Move left
                ans = mid
                right = mid - 1
            else:
                # Move right
                left = mid + 1

        return mid

    # Initialize tree
    tree = [0] * 4 * n
    arr = [1] * n
    stack = []
    cur = k
    init(0, n - 1, 1)

    for c in cmd:
        if c[0] == 'C':
            arr[cur] = 0
            stack.append(cur)
            # update segment tree
            update(0, n - 1, 1, cur, -1)

            # move cur
            if find_sum(0, n - 1, 1, 0, cur) == find_sum(0, n - 1, 1, 0, n - 1):
                cur = find_left(cur, 0)
            else:
                cur = find_right(cur, 1)

        elif c[0] == 'Z':
            temp = stack.pop()
            arr[temp] = 1
            update(0, n - 1, 1, temp, 1)
        else:
            count = int(c[2:])
            if c[0] == 'U':
                cur = find_left(cur, count)
            else:
                cur = find_right(cur, count)


    return ''.join(['O' if x == 1 else 'X' for x in arr])

#3. Solution using heap
# using min_heap to move down
# using max_heap to move up
# current is in the top of min_heap
import heapq
def solution(n, k, cmds):
    answer = ''
    def inverse(num):
        return -num
    max_heap = list(map(inverse,range(k)))
    min_heap = list(range(k,n))
    deleted = ['O' for _ in range(n)]
    deleted_stack = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for cmd in cmds:
        command = cmd.split()
        if len(command)>1:
            num = command[1]
            command = command[0]
            num = int(num)
            if command == 'D':
                for _ in range(num):
                    heapq.heappush(max_heap,-heapq.heappop(min_heap))
            else:
                for _ in range(num):
                    heapq.heappush(min_heap,-heapq.heappop(max_heap))
        else:
            command = command[0]
            if command == 'C':
                delete_num = heapq.heappop(min_heap)
                deleted_stack.append(delete_num)
                deleted[delete_num] = 'X'
                if len(min_heap) == 0:
                    heapq.heappush(min_heap,-heapq.heappop(max_heap))
            else:
                restore_num = deleted_stack.pop()
                deleted[restore_num] = 'O'
                if min_heap[0] > restore_num:
                    heapq.heappush(max_heap,-restore_num)
                else:
                    heapq.heappush(min_heap,restore_num)
    answer = ''.join(deleted)
    return answer
