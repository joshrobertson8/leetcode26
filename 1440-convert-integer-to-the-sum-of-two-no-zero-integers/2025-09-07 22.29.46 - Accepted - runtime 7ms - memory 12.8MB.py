"""
LeetCode: 2025 09 07 22.29.46 Accepted Runtime 7ms Memory 12.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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