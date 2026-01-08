"""
LeetCode: 2025 12 22 12.07.19 Accepted Runtime 550ms Memory 20.2MB

Algorithm:
Sort then two pointers: sort array. For each unique first element a, use two pointers (l, r) to find pairs that sum to -a. Skip duplicates for first element. When sum equals 0, add triplet, move l forward and skip duplicates. This finds all unique triplets summing to zero.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1                 # ← fix
                elif threeSum < 0:
                    l += 1                 # ← fix
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
