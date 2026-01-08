"""
LeetCode: 2025 12 20 14.59.10 Accepted Runtime 0ms Memory 18.5MB

Algorithm:
Use two pointers starting from both ends. If target is not in nums, return [-1, -1]. Move left pointer right while nums[l] < target. Move right pointer left while nums[r] > target. When both pointers stop moving, they point to the first and last occurrence of target. Return [l, r].

Time Complexity: O(n)
Space Complexity: O(1)
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