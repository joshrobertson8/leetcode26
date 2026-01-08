"""
LeetCode: 2024 12 30 12.40.32 Accepted Runtime 0ms Memory 13mb

Algorithm:
Sort citations in descending order. Create a mapping of rank (position) to citation value. The h-index is the maximum number of papers that have at least h citations. Count how many papers have citations >= their rank (1-indexed). Return the count.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_c = sorted(citations, reverse=True)
        ranks = {}
        rank = 1
        count = 0

        for i in range(len(sorted_c)):
            
            ranks[rank] = sorted_c[i]
            rank += 1

        for value, key in ranks.items():
            
            if key >= value:
                count += 1
        
        return count