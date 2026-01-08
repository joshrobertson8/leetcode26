"""
LeetCode: 2025 12 20 14.59.10 Accepted Runtime 0ms Memory 18.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1


        n = len(nums)

        if target not in nums: 
            return [-1, -1]
        while l <= r: 

            if nums[l] < target: 
                l += 1

            elif nums[r] > target: 
                r -= 1

            else:
                return [l, r]