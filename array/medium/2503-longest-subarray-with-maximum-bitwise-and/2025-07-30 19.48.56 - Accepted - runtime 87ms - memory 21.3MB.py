"""
LeetCode: 2025 07 30 19.48.56 Accepted Runtime 87ms Memory 21.3mb

Algorithm:
Find the maximum value in the array first. Then iterate through the array, tracking the length of consecutive elements equal to the maximum value. Reset the counter when encountering a non-maximum element. Return the longest consecutive sequence of maximum values, since bitwise AND of a subarray containing the maximum value can only be the maximum value itself.

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