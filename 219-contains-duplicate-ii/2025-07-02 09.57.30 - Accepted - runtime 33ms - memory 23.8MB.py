"""
LeetCode: 2025 07 02 09.57.30 Accepted Runtime 33ms Memory 23.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        lastSeen = {}

        for idx, val in enumerate(nums):

            if val in lastSeen and idx - lastSeen[val] <= k:
                return True
            lastSeen[val] = idx

        return False