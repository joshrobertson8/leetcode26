"""
LeetCode: 2024 10 07 09.27.10 Accepted Runtime 52ms Memory 13.2mb

Algorithm:
Use two pointers: k tracks the position to write unique elements, i scans through the array. Since the array is sorted, we only need to check if the current element differs from the previous one. When we find a new unique element, we write it at position k and increment k.

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