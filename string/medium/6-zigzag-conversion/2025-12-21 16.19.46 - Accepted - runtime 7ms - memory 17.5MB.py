"""
LeetCode: 2025 12 21 16.19.46 Accepted Runtime 7ms Memory 17.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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