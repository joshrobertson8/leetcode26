"""
LeetCode: 2025 09 25 23.48.27 Accepted Runtime 233ms Memory 31.3MB

Algorithm:
Use a set for O(1) lookup. Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def numIslands(self, grid):
        
        if not grid: 
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def explore(r, c): 

            queue = deque([(r, c)])
            visited.add((r, c))
            
            while queue: 
                row, col = queue.popleft()

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions: 
                    rowNeighbor, colNeighbor = row + dr, col + dc

                    # make sure we are in bounds, not visited, is land in the first place
                    if (0 <= rowNeighbor < rows and 0 <= colNeighbor < cols and
                    grid[rowNeighbor][colNeighbor] == "1" and (rowNeighbor, colNeighbor) not in visited): 

                        queue.append([rowNeighbor, colNeighbor])

                        visited.add((rowNeighbor, colNeighbor))

    
        
        for r in range(rows): 
            for c in range(cols): 

                if grid[r][c] == "1" and (r, c) not in visited: 
                    explore(r, c)
                    islands += 1

        return islands