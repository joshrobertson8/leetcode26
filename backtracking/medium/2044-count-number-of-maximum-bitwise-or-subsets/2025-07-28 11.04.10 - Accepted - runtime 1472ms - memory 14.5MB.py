"""
LeetCode: 2025 07 28 11.04.10 Accepted Runtime 1472ms Memory 14.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPossibleOr = 0 
        n = len(nums)
        count = 0

        for subset in range(1, 1 << n): 
            curOr = 0 

            for i in range(n): 

                if subset & (1 << i): 
                    curOr |= nums[i]
            
            if curOr > maxPossibleOr:
                maxPossibleOr = curOr
                count = 1
            
            elif curOr == maxPossibleOr: 
                count += 1
        return count