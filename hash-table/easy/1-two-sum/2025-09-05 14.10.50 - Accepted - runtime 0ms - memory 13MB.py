"""
LeetCode: 2025 09 05 14.10.50 Accepted Runtime 0ms Memory 13mb

Algorithm:
One-pass hash map: as we iterate, for each number calculate the complement needed. If complement exists in hash_table, return [hash_table[complement], i]. Otherwise, store current number and its index. This finds the pair in a single pass, more efficient than two-pass approach.

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
        # Use a hash table to store value -> index mapping
        hash_table = {}
        
        for i, num in enumerate(nums):
            # Calculate complement needed to reach target
            complement = target - num
            
            # Check if complement exists in hash table
            if complement in hash_table:
                return [hash_table[complement], i]
            
            # Store current number and its index
            hash_table[num] = i
        
        # Should never reach here given problem constraints
        return []