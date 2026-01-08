"""
LeetCode: 2024 10 02 15.40.46 Accepted Runtime 2199ms Memory 12.4mb

Algorithm:
Brute force: nested loops check all pairs (i, j) where j > i. If nums[i] + nums[j] == target, return [i, j]. This is O(n^2) time complexity, checking every possible pair combination.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]