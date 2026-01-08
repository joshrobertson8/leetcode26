"""
LeetCode: 2024 10 23 09.38.15 Accepted Runtime 11ms Memory 12.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        majority = len(nums) // 2

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            
            if hashmap[i] > majority:
                return i