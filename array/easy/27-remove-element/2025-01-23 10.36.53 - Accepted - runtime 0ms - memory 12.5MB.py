"""
LeetCode: 2025 01 23 10.36.53 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Iterate until condition is met.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        n = len(nums)

        while i < n:

            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n