"""
LeetCode: 2024 10 23 09.31.00 Accepted Runtime 13ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
    
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
    
        return candidate