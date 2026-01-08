"""
LeetCode: 2025 07 02 10.30.54 Accepted Runtime 83ms Memory 21.3MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        maxCount = 0
        curCount = 1

        for i in range(1, len(nums)):

            # skip a duplicate
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                curCount += 1

            else:
                maxCount = max(maxCount, curCount)
                curCount = 1

        return max(maxCount, curCount)
