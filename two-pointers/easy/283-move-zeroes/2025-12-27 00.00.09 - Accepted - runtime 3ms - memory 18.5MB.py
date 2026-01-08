"""
LeetCode: 2025 12 27 00.00.09 Accepted Runtime 3ms Memory 18.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        base = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[base] = nums[i]
                base += 1
            i += 1

        for i in range(base, len(nums)):
            nums[i] = 0