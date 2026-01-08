"""
LeetCode: 2025 03 10 17.54.07 Accepted Runtime 15ms Memory 12.4mb

Algorithm:
Create an array of empty strings, one for each row. Use a direction variable (1 for down, -1 for up) and a row pointer. For each character, add it to the current row's string. When reaching the top (row 0), change direction to down. When reaching the bottom (row numRows-1), change direction to up. Move the row pointer according to direction. Finally, join all rows.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        res = [""] * numRows

        row = 0 # row we are on
        direction = 1 # 1 means down, -1 means up 

        if numRows == 1 or len(s) < numRows:
            return s
        
        for char in s:
            res[row] += char

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(res)