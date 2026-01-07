"""
LeetCode: 2024 12 21 20.26.25 Accepted Runtime 36ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 1

        while i < len(nums):

            if nums[i] == nums[i - 1]:
                count += 1

                if count > 2:
                    nums.pop(i)
                    i -= 1
                    count -= 1
            else: 
                count = 1
            i += 1
        return len(nums)