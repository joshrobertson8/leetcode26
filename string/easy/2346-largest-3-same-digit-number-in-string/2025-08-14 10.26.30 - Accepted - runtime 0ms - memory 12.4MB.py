"""
LeetCode: 2025 08 14 10.26.30 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        maxGood = 0

        for i in range(1, len(num) - 1):
            good = 0

            if num[i - 1] == num[i] == num[i + 1]:
                good = num[i]
                maxGood = max(maxGood, good)
            
        return maxGood * 3 if maxGood != 0 else ""