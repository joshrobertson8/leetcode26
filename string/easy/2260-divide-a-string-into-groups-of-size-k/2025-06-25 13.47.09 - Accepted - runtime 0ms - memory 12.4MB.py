"""
LeetCode: 2025 06 25 13.47.09 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Chunk extraction: iterate through string in chunks of size k using while loop. Extract substring s[curr:curr+k] and append to result. Advance curr by k. After all chunks extracted, pad last chunk with fill character if its length < k (fill * (k - len(result[-1]))). This divides string into groups of size k, padding the last group if necessary.

Time Complexity: O(n)
Space Complexity: O(n)
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