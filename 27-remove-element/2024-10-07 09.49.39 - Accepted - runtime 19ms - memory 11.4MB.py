"""
LeetCode: 2024 10 07 09.49.39 Accepted Runtime 19ms Memory 11.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def removeElement(self, nums, val):
        while (nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)