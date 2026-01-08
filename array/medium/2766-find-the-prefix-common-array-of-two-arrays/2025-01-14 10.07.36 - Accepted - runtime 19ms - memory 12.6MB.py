"""
LeetCode: 2025 01 14 10.07.36 Accepted Runtime 19ms Memory 12.6mb

Algorithm:
Maintain two sets tracking elements seen so far in A and B. For each index i, add A[i] to a_vals and B[i] to b_vals. Count how many elements in a_vals also exist in b_vals (common elements up to index i). Append this count to the result array.

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

            for vals in a_vals:

                if vals in b_vals:
                    count += 1

            result.append(count)
        return result