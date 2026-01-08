"""
LeetCode: 2026 01 05 15.49.52 Accepted Runtime 8ms Memory 18MB

Algorithm:
Use a recursive helper function to explore all possibilities.

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
