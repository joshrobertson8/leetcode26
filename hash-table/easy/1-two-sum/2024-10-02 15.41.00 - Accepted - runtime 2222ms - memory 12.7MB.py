"""
LeetCode: 2024 10 02 15.41.00 Accepted Runtime 2222ms Memory 12.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]