"""
LeetCode: 2025 03 26 13.57.18 Accepted Runtime 0ms Memory 12.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
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