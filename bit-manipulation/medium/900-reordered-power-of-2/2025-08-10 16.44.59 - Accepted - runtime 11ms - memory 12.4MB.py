"""
LeetCode: 2025 08 10 16.44.59 Accepted Runtime 11ms Memory 12.4mb

Algorithm:
Use a Counter to count frequencies.

Time Complexity: O(n)
Space Complexity: O(n)
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