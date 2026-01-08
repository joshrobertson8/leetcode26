"""
LeetCode: 2025 08 05 17.40.17 Accepted Runtime 0ms Memory 13mb

Algorithm:
Iterate through each element with its index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash map: number → its index
        idx_by_val = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in idx_by_val:
                return [idx_by_val[need], i]
            idx_by_val[num] = i
        # The problem guarantees that a solution exists,
        # so this return will never be reached.
        return []