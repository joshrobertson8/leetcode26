"""
LeetCode: 2025 06 17 21.58.36 Accepted Runtime 2ms Memory 12.5mb

Algorithm:
Track the minimum value seen so far (minn). For each number, update the minimum, then calculate the difference between the current number and the minimum. Keep track of the maximum difference. If no positive difference is found (answer is 0), return -1, otherwise return the maximum difference.

Time Complexity: O(n)
Space Complexity: O(1)
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