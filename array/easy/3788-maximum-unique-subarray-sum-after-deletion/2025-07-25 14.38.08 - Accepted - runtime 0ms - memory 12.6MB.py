"""
LeetCode: 2025 07 25 14.38.08 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        maxSum = 0

        for num in nums: 

            if num > 0 and num not in seen:
                seen.add(num)
                maxSum += num

        if len(seen) == 0:
            return max(nums)
        
        return maxSum