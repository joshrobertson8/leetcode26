"""
LeetCode: 2024 12 13 20.48.28 Accepted Runtime 1ms Memory 12.1mb

Algorithm:
Use a set to track numbers we've seen. For each number, check if its double (2*i) exists in the set, or if it's even, check if its half (i/2) exists. If either condition is true, return True. Otherwise, add the current number to the set. This checks both directions (i*2 and i/2) to handle all cases.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for i in arr:
            if 2 * i in seen or ( i % 2 == 0 and i / 2 in seen):
                return True
            else:
                seen.add(i)

        return False