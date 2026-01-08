"""
LeetCode: 2026 01 06 11.18.52 Accepted Runtime 11ms Memory 20MB

Algorithm:
Two-pass DFS: first pass floods all border-connected 0s to 1s (not closed). Second pass counts remaining islands of 0s. For each remaining 0, start DFS to mark all connected 0s as 1s, incrementing closed island count. This identifies islands completely surrounded by 1s.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        closedIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c)
                    closedIslands += 1

        return closedIslands
