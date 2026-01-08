"""
LeetCode: 2024 11 09 20.39.06 Accepted Runtime 3ms Memory 12.2mb

Algorithm:
TODO: Describe your approach here

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