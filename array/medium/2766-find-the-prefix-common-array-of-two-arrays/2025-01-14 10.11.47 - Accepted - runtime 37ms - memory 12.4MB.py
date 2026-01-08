"""
LeetCode: 2025 01 14 10.11.47 Accepted Runtime 37ms Memory 12.4mb

Algorithm:
Build prefix array.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        result = 0 * []


        a_vals, b_vals = set(), set()

        for i in range(len(A)):

            a_vals.add(A[i])
            b_vals.add(B[i])

            count = 0 

            for val in a_vals:

                if val in b_vals:
                    count += 1

            result.append(count)
        return result