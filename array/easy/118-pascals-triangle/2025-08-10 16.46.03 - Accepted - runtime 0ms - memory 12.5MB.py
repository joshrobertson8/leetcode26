"""
LeetCode: 2025 08 10 16.46.03 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Build Pascal's triangle row by row. Start with the first row [1]. For each subsequent row, pad the previous row with zeros on both sides, then each element in the new row is the sum of two adjacent elements from the padded previous row.

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