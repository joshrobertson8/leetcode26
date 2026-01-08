"""
LeetCode: 2025 07 11 14.06.42 Accepted Runtime 13ms Memory 12.5mb

Algorithm:
Define a priority order for business lines. For each coupon, check if it's valid: code is non-empty, business line exists in order, and isActive is true. Also verify the code contains only alphanumeric characters and underscores. Store valid coupons with their priority, then sort by priority and return the codes.

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