"""
LeetCode: 2025 07 27 20.28.42 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
For each position, skip if it equals the previous element. Otherwise, find the closest non-equal left and right neighbors by scanning left and right until we find different values. If the current element is lower than both neighbors, it's a valley. If higher than both, it's a hill. After checking, jump to the right pointer position to avoid counting duplicates.

Time Complexity: O(n^2)
Space Complexity: O(1)
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