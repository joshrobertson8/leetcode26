"""
LeetCode: 2025 12 26 23.57.26 Accepted Runtime 7ms Memory 18.6MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
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