"""
LeetCode: 2024 10 09 09.30.13 Accepted Runtime 7308ms Memory 13.3mb

Algorithm:
Two-pass approach: first pass stores all indices in a map with index as key and value as value. Second pass, for each number, searches the entire map for complement, checking that the key is different from current index. This is inefficient O(n^2) due to nested iteration over map items.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        
        seen = {}
        

        for i in range(len(nums)):
            seen[i] = nums[i]
        
        # Iterate through the list to find the complement of each value
        for i in range(len(nums)):
            complement = target - nums[i]
            # Check if the complement exists in the seen dictionary values
            for key, value in seen.items():
                if value == complement and key != i:
                    # Return the indices of the two numbers that add up to the target
                    return [i, key]
        
        # If no valid pair is found, return an empty list
        return []