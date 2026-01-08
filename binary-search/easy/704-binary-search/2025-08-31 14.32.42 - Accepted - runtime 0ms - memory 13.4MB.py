"""
LeetCode: 2025 08 31 14.32.42 Accepted Runtime 0ms Memory 13.4MB

Algorithm:
Continue until condition is met.

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