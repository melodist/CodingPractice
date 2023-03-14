"""
https://leetcode.com/problems/surrounded-regions
Change surrounded "O" by dummy and change other "O" with "X"
"""
#1. Solution using union-find (296ms)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return

        m = len(board)
        n = len(board[0])

        uf = UnionFind(m * n + 1)
        dummy = m * n

        # connect 'O' at first and last col with dummy
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(dummy, i * n)
            if board[i][-1] == 'O':
                uf.union(dummy, i * n + n - 1)

        # connect 'O' at first and last row with dummy
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(dummy, j)
            if board[-1][j] == 'O':
                uf.union(dummy, n * (m-1) + j)

        d = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for di, dj in d:
                        x = i+di
                        y = j+dj
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)

        # change not connected 'O' with 'X'
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'

class UnionFind:
    def __init__(self, size):
        self.count = size
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return

        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]

        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def count(self):
        return self.count
