"""
LeetCode: 2025 08 10 16.45.05 Accepted Runtime 14ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occurance = Counter(str(n))

        for i in range(30): 
            if occurance == Counter(str(2 ** i)): 
                return True
        return False