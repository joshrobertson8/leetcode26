"""
LeetCode: 2025 07 27 20.55.13 Accepted Runtime 0ms Memory 12.4mb

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
        i = 1

        while i < len(nums):
            
            cur = nums[i]

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

            i = right 

        return hills + vallys