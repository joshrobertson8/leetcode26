"""
LeetCode: 2024 10 09 15.52.22 Accepted Runtime 738ms Memory 13.7mb

Algorithm:
Iterate through nums.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def singleNumber(self, nums):
        
        seen = []

        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                seen.remove(i)
        return seen[0]