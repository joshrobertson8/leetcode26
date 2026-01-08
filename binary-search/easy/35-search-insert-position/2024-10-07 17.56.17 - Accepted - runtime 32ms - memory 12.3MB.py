"""
LeetCode: 2024 10 07 17.56.17 Accepted Runtime 32ms Memory 12.3mb

Algorithm:
Linear search: iterate through the array. If target equals current element, return that index. If target is less than or equal to current element, return current index (insert here). If we reach the end without finding a position, return len(nums) (insert at end).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def searchInsert(self, nums, target):
        
        
        for i in range(len(nums)):

            if target == nums[i]:
                return i

            if target <= nums[i]:
                return i
        return i + 1