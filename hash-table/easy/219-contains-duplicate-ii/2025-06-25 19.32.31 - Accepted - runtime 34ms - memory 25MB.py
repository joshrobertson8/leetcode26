"""
LeetCode: 2025 06 25 19.32.31 Accepted Runtime 34ms Memory 25mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}

        for i in range(len(nums)):

            if nums[i] in hashmap:
                if i - hashmap[nums[i]] <= k:
                    return True

            hashmap[nums[i]] = i

        return False