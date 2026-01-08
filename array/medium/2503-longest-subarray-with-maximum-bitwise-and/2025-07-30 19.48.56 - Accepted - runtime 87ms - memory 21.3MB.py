"""
LeetCode: 2025 07 30 19.48.56 Accepted Runtime 87ms Memory 21.3mb

Algorithm:
Use two pointers moving toward each other.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        current = 0 
        longest = 0

        for num in nums: 

            if num == maxVal:
                current += 1

            else:
                current = 0
            
            longest = max(longest, current)

        return longest