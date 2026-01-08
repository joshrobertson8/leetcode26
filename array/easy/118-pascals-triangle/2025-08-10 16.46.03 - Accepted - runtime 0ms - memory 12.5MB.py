"""
LeetCode: 2025 08 10 16.46.03 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = [[1]]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            result.append(row)
        return result