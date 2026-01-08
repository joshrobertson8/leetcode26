"""
LeetCode: 2024 11 09 20.39.06 Accepted Runtime 3ms Memory 12.2mb

Algorithm:
Create a new result array. Iterate through the original array: for each zero, append two zeros to the result; for each non-zero, append it once. Then copy the first len(arr) elements from the result back into the original array. This handles the duplication in-place by using a temporary array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        result = []

        for i in range(len(arr)):
            if arr[i] == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(arr[i])

        for i in range(len(arr)):
            arr[i] = result[i]