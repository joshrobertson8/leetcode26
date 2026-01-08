"""
LeetCode: 2026 01 01 17.21.43 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1

        return write