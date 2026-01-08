"""
LeetCode: 2025 12 21 00.35.35 Accepted Runtime 0ms Memory 17MB

Algorithm:
Two-step rotation: first transpose matrix (swap matrix[i][j] with matrix[j][i] for i < j). Then reflect each row (swap matrix[i][j] with matrix[i][n-1-j] for j < n//2). This rotates 90 degrees clockwise in-place.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        

    def transpose(self, matrix):

        for i in range(len(matrix)): 
            for j in range(i , len(matrix)): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)

        for i in range(n): 
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

