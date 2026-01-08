"""
LeetCode: 2025 02 20 00.35.32 Accepted Runtime 3ms Memory 12.9mb

Algorithm:
Linear search: iterate through the array. If current element is greater than or equal to target, return that index (insert here). If we reach the end without finding such position, return len(nums) (insert at end).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def searchInsert(self, nums, target):

        for i in range(len(nums)):
            
            if nums[i] >= target:
                return i
        return len(nums)