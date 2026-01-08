"""
LeetCode: 2025 01 30 14.18.40 Accepted Runtime 532ms Memory 18.2mb

Algorithm:
Sort then two pointers: sort array. For each unique first element nums[i], use two pointers (lo, hi) to find pairs that sum to -nums[i]. Skip duplicates for first element. When sum equals 0, add triplet, move both pointers, skip duplicates for lo. This finds all unique triplets summing to zero.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1