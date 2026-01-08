"""
LeetCode: 2024 10 07 09.49.43 Accepted Runtime 16ms Memory 11.4MB

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