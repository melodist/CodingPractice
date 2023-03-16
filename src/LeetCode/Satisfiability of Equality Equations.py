"""
https://leetcode.com/problems/satisfiability-of-equality-equations
Using union-find
"""
#1. My Solution (52ms)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for eq in equations:
            if eq[1] == '=':
                uf.union(ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a'))

        for eq in equations:
            if eq[1] == '!':
                if uf.connected(ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')):
                    return False

        return True

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
      
#2. Other Solution (34ms)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality = defaultdict(set)
        for x_i, eq, _, y_i in equations:
            if eq == '=':
                new_grp = {x_i, y_i}
                new_grp = new_grp.union(equality[x_i])
                new_grp = new_grp.union(equality[y_i])
                for char in new_grp:
                    equality[char] = new_grp

        for x_i, eq, _, y_i in equations:
            if eq == '!':
                if x_i == y_i:
                    return False
                if x_i in equality[y_i]:
                    return False
        return True
