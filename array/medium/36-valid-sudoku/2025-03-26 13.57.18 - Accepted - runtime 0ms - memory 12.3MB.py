"""
LeetCode: 2025 03 26 13.57.18 Accepted Runtime 0ms Memory 12.3mb

Algorithm:
Use three sets of sets: one for rows, one for columns, and one for 3x3 boxes. For each cell, if it's not empty, check if the value already exists in the corresponding row, column, or box set. If it does, return False. Otherwise, add it to all three sets. Calculate box index as (r//3)*3 + c//3. If all cells pass, return True.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                index = (r // 3) * 3 + c // 3

                if val in boxes[index]:
                    return False
                boxes[index].add(val)

        return True