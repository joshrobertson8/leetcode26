"""
LeetCode: 2024 10 02 15.41.00 Accepted Runtime 2222ms Memory 12.7mb

Algorithm:
Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]