"""
LeetCode: 2026 01 01 15.07.38 Accepted Runtime 263ms Memory 24.9MB

Algorithm:
BFS traversal: iterate through each cell. When finding an unvisited '1', start BFS using a queue to mark all connected '1's as visited. BFS explores 4-directional neighbors that are '1' and unvisited. Each BFS call marks one island. Count the number of BFS starts.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def numIslands(self, grid):
        # solve with a bfs

        if not grid: 
            return -1

        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        
        def explore(r, c): 
            Q = deque([(r, c)])
            visited.add((r, c))
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

            while Q: 
                row, col = Q.popleft()

                for rn, cn in directions: 
                    rn, cn = row + rn, col + cn

                    if 0 <= rn < rows and 0 <= cn < cols and (rn, cn) not in visited and grid[rn][cn] == "1": 
                        Q.append((rn, cn))

                        visited.add((rn, cn))

        
        for r in range(rows): 
            for c in range(cols): 

                if (r, c) not in visited and grid[r][c] == "1": 
                    explore(r, c)

                    islands += 1

        return islands