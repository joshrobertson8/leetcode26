"""
LeetCode: 2024 10 09 09.30.13 Accepted Runtime 7308ms Memory 13.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
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