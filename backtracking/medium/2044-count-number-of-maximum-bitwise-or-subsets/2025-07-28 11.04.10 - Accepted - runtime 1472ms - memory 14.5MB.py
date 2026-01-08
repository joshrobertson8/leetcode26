"""
LeetCode: 2025 07 28 11.04.10 Accepted Runtime 1472ms Memory 14.5MB

Algorithm:
Generate all possible subsets using bit manipulation. For each subset (represented as a bitmask from 1 to 2^n-1), compute the OR of all numbers in that subset. Track the maximum OR value seen and count how many subsets achieve it. For each subset, iterate through bits to determine which numbers to include, then compute their OR.

Time Complexity: O(n^2)
Space Complexity: O(1)
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