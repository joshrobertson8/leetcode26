"""
LeetCode: 2025 07 31 14.11.04 Accepted Runtime 476ms Memory 36.7mb

Algorithm:
For each element, maintain a set of all possible OR values ending at that position. Start with the current element. For each previous OR value, compute its OR with the current element and add to the current set. Update the result set with all values in the current set. The previous set represents all OR values from subarrays ending at the previous position. This efficiently tracks all distinct OR values.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        result = set()
        previous = set()

        for num in arr: 

            current = {num}

            for val in previous: 

                current.add( val | num )
            
            result.update(current)
            previous = current
            
        return len(result)