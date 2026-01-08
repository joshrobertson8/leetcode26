"""
LeetCode: 2025 12 17 00.16.40 Accepted Runtime 0ms Memory 18.1MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        originalColor = image[sr][sc]

        if color == originalColor: 
            return image

        rows, cols = len(image), len(image[0])

        visited = set()

        def bfs(r, c): 
            Q = deque([(r, c)])
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while Q: 
                row, col = Q.popleft()

                image[row][col] = color

                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and image[nr][nc] == originalColor: 
                        visited.add((nr, nc))
                        Q.append((nr, nc))

        bfs(sr, sc)
        return image