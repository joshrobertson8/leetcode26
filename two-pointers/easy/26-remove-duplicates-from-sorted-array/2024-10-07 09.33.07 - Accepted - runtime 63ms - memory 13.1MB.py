"""
LeetCode: 2024 10 07 09.33.07 Accepted Runtime 63ms Memory 13.1MB

Algorithm:
Iterate through the array once.

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
        