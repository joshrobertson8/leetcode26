"""
LeetCode: 2025 06 17 21.56.43 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Track the minimum value seen so far (candidate). For each number, update the minimum candidate, then calculate the difference between the current number and the minimum. Keep track of the maximum difference. If no positive difference is found (answer is 0), return -1, otherwise return the maximum difference.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        candidate = float('inf')
        answer = 0

        for num in nums:

            candidate = min(candidate, num)

            answer = max(answer, num - candidate)


        return -1 if answer == 0 else answer