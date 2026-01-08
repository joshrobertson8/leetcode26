"""
LeetCode: 2025 02 20 00.41.40 Accepted Runtime 0ms Memory 12.9mb

Algorithm:
Binary search to find insertion position. If target is found, return its index. If nums[pivot] >= target, search left half (including pivot). Otherwise, search right half. When loop exits, left points to the insertion position (first position where element >= target).

Time Complexity: O(n)
Space Complexity: O(1)
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