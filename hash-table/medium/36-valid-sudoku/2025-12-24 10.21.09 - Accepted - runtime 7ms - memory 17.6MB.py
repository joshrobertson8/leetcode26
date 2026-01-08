"""
LeetCode: 2025 12 24 10.21.09 Accepted Runtime 7ms Memory 17.6MB

Algorithm:
Use three sets of sets: one for rows, one for columns, and one for 3x3 boxes. For each cell, if it's not empty, check if the value already exists in the corresponding row, column, or box set. If it does, return False. Otherwise, add it to all three sets. Calculate box index as (r//3)*3 + c//3. If all cells pass, return True.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [set() for r in range(n)]
        cols = [set() for c in range(n)]
        boxes = [set() for b in range(n)]

        for r in range(n):
            for c in range(n):

                cur = board[r][c]

                if cur == '.':
                    continue

                if cur in rows[r]: 
                    return False
                
                if cur in cols[c]: 
                    return False

                rows[r].add(cur)
                cols[c].add(cur)

                box = (r // 3) * 3 + (c // 3)

                if cur in boxes[box]: 
                    return False
                boxes[box].add(cur)
        return True