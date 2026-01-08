"""
LeetCode: 2024 10 03 02.42.44 Accepted Runtime 84ms Memory 13.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result