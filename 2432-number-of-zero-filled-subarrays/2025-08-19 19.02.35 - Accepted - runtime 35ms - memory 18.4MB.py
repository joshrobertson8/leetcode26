"""
LeetCode: 2025 08 19 19.02.35 Accepted Runtime 35ms Memory 18.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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