"""
LeetCode: 2025 03 26 13.57.18 Accepted Runtime 0ms Memory 12.3MB

Algorithm:
Set-based validation: use three sets of sets - rows, cols, and boxes (3x3 subgrids). Iterate through each cell: if value is '.', skip. Otherwise check if value exists in corresponding row set, column set, or box set. If found in any, sudoku is invalid. Otherwise add to all three sets. Box index calculated as (r // 3) * 3 + c // 3. This validates that no digit repeats in row, column, or 3x3 box.

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