"""
LeetCode: 2025 07 02 09.57.30 Accepted Runtime 33ms Memory 23.8mb

Algorithm:
Use hash map to track last seen index for each value. For each number, if it exists in map and current index - last seen index <= k, return True (duplicate within k distance). Otherwise, update the last seen index. This checks for duplicates within window k in one pass.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        lastSeen = {}

        for idx, val in enumerate(nums):

            if val in lastSeen and idx - lastSeen[val] <= k:
                return True
            lastSeen[val] = idx

        return False