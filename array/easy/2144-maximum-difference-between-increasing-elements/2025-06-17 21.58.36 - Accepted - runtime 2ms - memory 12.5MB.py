"""
LeetCode: 2025 06 17 21.58.36 Accepted Runtime 2ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minn = float('inf')
        answer = 0

        for num in nums:

            minn = min(minn, num)

            answer = max(answer, num - minn)


        return -1 if answer == 0 else answer