"""
LeetCode: 2025 07 11 13.34.11 Accepted Runtime 4ms Memory 13mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [] 

        for num in nums:

            if num % 2 == 0:
                result.append(num)

        for num in nums:
            if num % 2 != 0:
                result.append(num)

        return result