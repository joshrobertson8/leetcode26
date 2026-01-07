"""
LeetCode: 2025 02 20 00.41.40 Accepted Runtime 0ms Memory 12.9mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def searchInsert(self, nums, target):

        left = 0 
        right = len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left