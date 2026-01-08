"""
LeetCode: 2025 12 21 16.19.23 Accepted Runtime 11ms Memory 17.3MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows

        
        row = 0
        direction = 1
        
        if numRows == 1 or len(s) < numRows:
            return s
        
        for ch in s: 
            res[row] += ch

            if row == 0: 
                direction = 1
            
            elif row == numRows - 1: 
                direction = -1

            row += direction

        return "".join(res)