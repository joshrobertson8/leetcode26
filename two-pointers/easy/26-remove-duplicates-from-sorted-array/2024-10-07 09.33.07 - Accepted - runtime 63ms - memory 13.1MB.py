"""
LeetCode: 2024 10 07 09.33.07 Accepted Runtime 63ms Memory 13.1MB

Algorithm:
Two pointers for sorted array: use k as write pointer starting at 1 (first element is always unique). Iterate from index 1: if nums[i] != nums[i-1], it's a new unique element, write to nums[k] and increment k. This removes duplicates in-place for sorted arrays, keeping only unique elements. Return k (number of unique elements).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        
        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
        