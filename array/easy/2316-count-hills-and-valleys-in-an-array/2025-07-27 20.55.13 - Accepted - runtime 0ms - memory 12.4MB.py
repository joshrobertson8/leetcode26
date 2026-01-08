"""
LeetCode: 2025 07 27 20.55.13 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Use a while loop to iterate through positions. For each position, find the closest non-equal left and right neighbors by scanning left and right until we find different values. If the current element is higher than both neighbors, it's a hill. If lower than both, it's a valley. After checking, jump to the right pointer position to avoid counting duplicates.

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