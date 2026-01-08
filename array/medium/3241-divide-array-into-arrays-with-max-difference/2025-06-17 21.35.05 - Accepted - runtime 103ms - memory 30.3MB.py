"""
LeetCode: 2025 06 17 21.35.05 Accepted Runtime 103ms Memory 30.3mb

Algorithm:
Sort the array first.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()

        n = len(nums)

        answer = []

        for i in range(0, n, 3):

            if nums[i + 2] - nums[i] > k:
                return []

            answer.append([nums[i], nums[i + 1], nums[i + 2]])

        return answer

        return nums