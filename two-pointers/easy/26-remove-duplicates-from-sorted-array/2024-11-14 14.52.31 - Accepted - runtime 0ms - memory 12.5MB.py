"""
LeetCode: 2024 11 14 14.52.31 Accepted Runtime 0ms Memory 12.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        
        unique_elements = {}
        k = 0  # Counter for the number of unique elements

    # Traverse through the array
        for i in nums:
            # If the number is not in the dictionary, it's unique
            if i not in unique_elements:
                unique_elements[i] = 0
                # Place the unique element in the 'nums' array at the 'k' position
                nums[k] = i
                k += 1

        # k now represents the number of unique elements
        return k