"""
LeetCode: 2024 10 23 09.50.48 Accepted Runtime 15ms Memory 13mb

Algorithm:
Use a hash map to track seen values.

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