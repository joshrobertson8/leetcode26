"""
LeetCode: 2025 01 14 10.18.17 Accepted Runtime 11ms Memory 12.5mb

Algorithm:
Build prefix array.

Time Complexity: O(n)
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
        count = 0

        for i in range(len(A)):

            if A[i] == B[i]:
                count += 1

            else:
                a_vals.add(A[i])
                b_vals.add(B[i])

                if A[i] in b_vals:
                    count += 1
                if B[i] in a_vals:
                    count += 1

            result.append(count)
        return result