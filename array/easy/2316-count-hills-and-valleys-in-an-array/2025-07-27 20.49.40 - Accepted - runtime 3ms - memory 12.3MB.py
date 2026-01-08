"""
LeetCode: 2025 07 27 20.49.40 Accepted Runtime 3ms Memory 12.3mb

Algorithm:
Use two pointers moving toward each other.

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

            if cur == nums[i - 1]:
                continue

            left = i - 1
            while left > 0 and nums[left] == cur: 
                left -=1
            
            right = i + 1
            while right < len(nums) and nums[right] == cur:
                right += 1

            
            if left >= 0 and right < len(nums):
                if cur > nums[right] and cur > nums[left]:
                    hills +=1
                
                elif cur < nums[right] and cur < nums[left]:
                    vallys += 1

        return hills + vallys