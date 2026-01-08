"""
LeetCode: 2024 10 07 09.47.49 Accepted Runtime 15ms Memory 11.5mb

Algorithm:
Use two pointers: k tracks where to write elements that should be kept, i scans through the array. For each element, if it's not equal to val, we copy it to position k and increment k. This effectively shifts all non-val elements to the front.

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