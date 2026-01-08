"""
LeetCode: 2025 07 31 14.11.04 Accepted Runtime 476ms Memory 36.7mb

Algorithm:
Use a set for O(1) lookup. Use two pointers moving toward each other.

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