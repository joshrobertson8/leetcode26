"""
LeetCode: 2025 08 31 14.26.12 Accepted Runtime 0ms Memory 13.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right: 

            mid = (left + right) // 2

            if nums[mid] == target: 
                return mid
            
            elif nums[mid] < target: 
                left = mid + 1
            
            else: 
                right = mid - 1
        
        return -1