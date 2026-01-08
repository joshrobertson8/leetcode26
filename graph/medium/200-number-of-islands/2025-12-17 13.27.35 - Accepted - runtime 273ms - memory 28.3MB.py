"""
LeetCode: 2025 12 17 13.27.35 Accepted Runtime 273ms Memory 28.3MB

Algorithm:
DFS traversal: iterate through each cell. When finding an unvisited '1', start DFS to mark all connected '1's as visited. DFS explores 4-directional neighbors that are '1' and unvisited. Each DFS call marks one island. Count the number of DFS starts.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List, Set, Tuple

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c): 
            visited.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


            for dr, dc in directions: 

                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1": 
                    dfs(nr, nc)

        for r in range(rows): 
            for c in range(cols): 

                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands