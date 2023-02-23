"""
https://leetcode.com/problems/sliding-puzzle
Using BFS
"""
#1. My Solution (39ms)
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap_pos(string, a, b):
            lst = list(string)
            lst[a], lst[b] = lst[b], lst[a]
            return ''.join(lst)

        neighbor = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        visited = set()
        solved = '123450'
        puzzle = reduce(lambda acc, cur: acc + ''.join([str(x) for x in cur]), board, "")

        q = deque([(puzzle, 0)])

        while q:
            curr, count = q.popleft()
            if curr == solved:
                return count

            pos_zero = curr.find('0')
            for pos_swap in neighbor[pos_zero]:
                next = swap_pos(curr, pos_zero, pos_swap)
                if next not in visited:
                    q.append((next, count+1))

                visited.add(next)

        return -1
