"""
LeetCode: 2025 12 24 10.21.09 Accepted Runtime 7ms Memory 17.6MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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