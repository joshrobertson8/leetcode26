"""
LeetCode: 2025 06 25 19.32.31 Accepted Runtime 34ms Memory 25mb

Algorithm:
Use hash map to track last seen index for each value. For each number, if it exists in map and current index - last seen index <= k, return True (duplicate within k distance). Otherwise, update the last seen index. This checks for duplicates within window k in one pass.

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