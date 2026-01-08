"""
LeetCode: 2025 07 11 13.34.11 Accepted Runtime 4ms Memory 13mb

Algorithm:
Two-pass approach: first pass collects all even numbers, second pass collects all odd numbers. Append them in order. This separates evens and odds, placing evens first, then odds. O(n) time but requires extra space.

Time Complexity: O(n)
Space Complexity: O(n)
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