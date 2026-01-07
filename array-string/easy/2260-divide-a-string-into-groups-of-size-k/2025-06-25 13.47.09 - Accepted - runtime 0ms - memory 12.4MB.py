"""
LeetCode: 2025 06 25 13.47.09 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        result = []
        
        n = len(s)

        curr = 0

        while curr < n:
            result.append(s[curr:curr + k])
            curr +=k

        result[-1] += fill * (k-len(result[-1]))
        return result