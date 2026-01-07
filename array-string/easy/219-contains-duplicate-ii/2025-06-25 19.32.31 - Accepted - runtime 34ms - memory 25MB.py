"""
LeetCode: 2025 06 25 19.32.31 Accepted Runtime 34ms Memory 25mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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