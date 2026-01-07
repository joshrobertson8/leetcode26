"""
LeetCode: 2025 07 27 20.28.42 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vallys = 0 
        hills = 0

        for i in range(1, len(nums) - 1):
            cur = nums[i]

            if nums[i] == nums[i - 1]:
                continue

            # Find closest non-equal left neighbor
            left = i - 1
            while left >= 0 and nums[left] == cur:
                left -= 1

            # Find closest non-equal right neighbor
            right = i + 1
            while right < len(nums) and nums[right] == cur:
                right += 1

            # Make sure both neighbors are valid before comparing
            if left >= 0 and right < len(nums):
                if cur < nums[left] and cur < nums[right]:
                    vallys += 1
                elif cur > nums[left] and cur > nums[right]:
                    hills += 1
            i = right 

        return hills + vallys