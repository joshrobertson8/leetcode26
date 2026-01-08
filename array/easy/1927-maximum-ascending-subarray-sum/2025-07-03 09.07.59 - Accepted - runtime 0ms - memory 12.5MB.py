"""
LeetCode: 2025 07 03 09.07.59 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Greedy algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = 0 
        curSum = nums[0]

        for num in range(1, len(nums)):

            if nums[num - 1] < nums[num]:
                curSum += nums[num]

            else:
                maxSum = max(maxSum, curSum)
                curSum = nums[num]

        return max(curSum, maxSum)