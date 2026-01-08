"""
LeetCode: 2025 08 31 14.32.42 Accepted Runtime 0ms Memory 13.4MB

Algorithm:
Standard binary search: maintain left and right pointers. Calculate mid point. If nums[mid] equals target, return mid. If nums[mid] is greater than target, search left half by setting right = mid - 1. Otherwise, search right half by setting left = mid + 1. If loop exits without finding target, return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = (r + l) // 2

            if nums[mid] == target: 
                return mid

            elif nums[mid] > target: 
                r = mid - 1

            else: 
                l = mid + 1

        return -1