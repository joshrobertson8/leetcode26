"""
LeetCode: 2025 02 26 14.09.42 Accepted Runtime 95ms Memory 20.4mb

Algorithm:
Use Kadane's algorithm variant to find both maximum and minimum subarray sums simultaneously. Track cur_max and cur_min: cur_max extends the maximum sum ending at current position, cur_min extends the minimum sum. Update global max_sum and min_sum. The maximum absolute sum is the maximum of abs(min_sum) and max_sum, since absolute value can come from either extreme.

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