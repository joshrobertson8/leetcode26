"""
LeetCode: 2025 08 19 19.02.35 Accepted Runtime 35ms Memory 18.4mb

Algorithm:
Maintain a count of consecutive zeros. For each element, if it's zero, increment the count. Otherwise, reset count to 0. For each consecutive zero sequence of length n, it contributes n subarrays ending at that position (subarrays of lengths 1, 2, ..., n). Add the current count to the answer at each step. This accumulates all zero-filled subarrays.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        answer = 0 

        for num in nums:

            if num == 0: 
                count += 1
            else: 
                count = 0
            answer += count
            
        return answer