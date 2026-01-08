"""
LeetCode: 2025 09 07 22.29.46 Accepted Runtime 7ms Memory 12.8mb

Algorithm:
Try all possible pairs (num1, num2) where num1 + num2 = n. For each num1 from 1 to n-1, calculate num2 = n - num1. Convert both to strings and check if either contains '0'. If neither contains '0', return the pair. This finds the first valid pair.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        for num1 in range(1, n):

            num2 = n - num1

            if "0" not in str(num1) + str(num2):

                return [num1, num2]
        return []