"""
https://leetcode.com/problems/loud-and-rich/
Using cached DFS
Don't find all connections first, just use DFS.
"""
#1. My Solution
class Solution(object):
    def loudAndRich(self, richer, quiet):
        m = collections.defaultdict(list)
        for i, j in richer: m[j].append(i)
        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] >= 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]: res[i] = res[j]
            return res[i]

        for i in range(len(quiet)): dfs(i)
        return res
