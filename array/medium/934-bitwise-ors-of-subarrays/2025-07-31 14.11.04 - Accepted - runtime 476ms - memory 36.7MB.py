"""
LeetCode: 2025 07 31 14.11.04 Accepted Runtime 476ms Memory 36.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
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