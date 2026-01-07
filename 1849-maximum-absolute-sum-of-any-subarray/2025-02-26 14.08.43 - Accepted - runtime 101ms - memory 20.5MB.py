"""
LeetCode: 2025 02 26 14.08.43 Accepted Runtime 101ms Memory 20.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = min_sum = 0 

        cur_max = cur_min = 0 

        for i in nums:

            cur_max = max(i, cur_max + i)
            max_sum = max(max_sum, cur_max)

            cur_min = min(i, cur_min + i)
            min_sum = min(min_sum, cur_min)
        return max(abs(min_sum), max_sum)