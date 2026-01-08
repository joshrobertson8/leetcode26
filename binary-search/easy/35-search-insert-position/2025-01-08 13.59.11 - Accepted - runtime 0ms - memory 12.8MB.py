"""
LeetCode: 2025 01 08 13.59.11 Accepted Runtime 0ms Memory 12.8mb

Algorithm:
Linear search: iterate through the array. If target equals current element, return that index. If current element is greater than target, return current index (insert here). If we reach the end without finding a position, return len(nums) (insert at end).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def searchInsert(self, nums, target):

        for i in range(len(nums)):

            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)