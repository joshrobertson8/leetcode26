"""
LeetCode: 2024 10 07 09.49.39 Accepted Runtime 19ms Memory 11.4mb

Algorithm:
Iterate until condition is met.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        while (nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)