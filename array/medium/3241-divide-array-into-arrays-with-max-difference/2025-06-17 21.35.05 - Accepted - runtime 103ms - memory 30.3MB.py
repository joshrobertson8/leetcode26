"""
LeetCode: 2025 06 17 21.35.05 Accepted Runtime 103ms Memory 30.3mb

Algorithm:
Sort the array first. Then group elements into triplets starting from index 0, 3, 6, etc. For each triplet [i, i+1, i+2], check if the difference between the maximum (nums[i+2]) and minimum (nums[i]) exceeds k. If any triplet violates this constraint, return empty array. Otherwise, return the array of triplets.

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