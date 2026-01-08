"""
LeetCode: 2025 08 10 16.44.57 Accepted Runtime 11ms Memory 12.5mb

Algorithm:
Count the frequency of each digit in n using Counter. Then check all powers of 2 up to 2^30. For each power of 2, count its digit frequencies. If the frequency counts match exactly, n can be reordered to form that power of 2. Return True if any match is found, False otherwise.

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