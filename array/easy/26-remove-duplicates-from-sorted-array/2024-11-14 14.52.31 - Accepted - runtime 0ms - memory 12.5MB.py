"""
LeetCode: 2024 11 14 14.52.31 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Use a hash table (dictionary) to track which elements we've already seen. As we iterate through the array, if an element hasn't been seen before, we add it to the dictionary and write it at position k. This approach works for unsorted arrays but uses extra space.

Time Complexity: O(n)
Space Complexity: O(n)
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