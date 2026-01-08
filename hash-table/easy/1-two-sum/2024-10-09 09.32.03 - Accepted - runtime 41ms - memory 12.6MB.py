"""
LeetCode: 2024 10 09 09.32.03 Accepted Runtime 41ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self,nums,target):
        # Example using hashmap with value as key and index as value
        hashmap = {}
        
        # Populate the hashmap with each value in the list and its index
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        # Iterate through the list to find the complement of each value
        for i in range(len(nums)):
            complement = target - nums[i]
            # Check if the complement exists in the hashmap and is not the current index
            if complement in hashmap and hashmap[complement] != i:
                # Return the indices of the two numbers that add up to the target
                return [i, hashmap[complement]]
        
        # If no valid pair is found, return an empty list
        return []