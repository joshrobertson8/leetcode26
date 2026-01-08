"""
LeetCode: 2024 10 23 09.38.15 Accepted Runtime 11ms Memory 12.8mb

Algorithm:
Build frequency map counting occurrences. Track majority threshold (len(nums) // 2). As we count, if any number's frequency exceeds majority threshold, return it immediately. This early termination optimizes the hash map approach.

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