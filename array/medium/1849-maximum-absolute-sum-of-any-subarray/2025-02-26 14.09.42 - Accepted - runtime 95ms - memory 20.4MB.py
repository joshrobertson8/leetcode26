"""
LeetCode: 2025 02 26 14.09.42 Accepted Runtime 95ms Memory 20.4mb

Algorithm:
Greedy algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
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