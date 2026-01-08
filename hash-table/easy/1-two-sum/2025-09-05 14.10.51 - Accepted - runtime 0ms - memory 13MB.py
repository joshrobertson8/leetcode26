"""
LeetCode: 2025 09 05 14.10.51 Accepted Runtime 0ms Memory 13MB

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

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