"""
LeetCode: 2025 07 11 14.06.42 Accepted Runtime 13ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        result = []

        for c, b, a in zip(code, businessLine, isActive):
            if not c or b not in order or not a:
                continue

            if all(ch.isalnum() or ch == "_" for ch in c):
                result.append((order[b], c))

        result.sort()
        return [c for _, c in result]