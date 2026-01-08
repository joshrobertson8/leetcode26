"""
LeetCode: 2024 10 09 11.34.33 Accepted Runtime 3166ms Memory 196.1mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        status = [0] * n
        graph = [[] for _ in range(n)]
        external_invocation = [False]

        for a, b in invocations:
            graph[a].append(b)

        def dfs(method):
            if status[method] == 2:
                return
            if status[method] == 1:
                return
            
            status[method] = 1
            for callee in graph[method]:
                dfs(callee)
            status[method] = 2

        dfs(k)


        for a, b in invocations:
            if status[b] != 0 and status[a] == 0:
                return list(range(n))

        return [i for i in range(n) if status[i] != 1 and status[i] != 2]