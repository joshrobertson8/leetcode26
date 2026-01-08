"""
LeetCode: 2025 07 25 14.38.08 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Use a set to track which positive numbers we've already seen. Iterate through the array, and for each positive number that hasn't been seen, add it to the set and add it to the running sum. If no unique positive numbers were found, return the maximum value in the array (handles all negative/zero case).

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