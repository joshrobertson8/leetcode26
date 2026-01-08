"""
LeetCode: 2024 10 07 09.47.52 Accepted Runtime 18ms Memory 11.4mb

Algorithm:
Iterate through the array once.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k