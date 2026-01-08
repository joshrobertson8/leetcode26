"""
LeetCode: 2025 07 14 08.29.41 Accepted Runtime 0ms Memory 12.6MB

Algorithm:
Traverse list and collect bits into array. Reverse array and compute decimal: for each bit at index i, add bit * 2^i. This processes bits from least significant to most significant. Return sum.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        storage = []
        result = 0 

        current = head

        while current:
            storage.append(current.val)
            current = current.next

        for idx, val in enumerate(reversed(storage)):
            result += val * 2 ** idx
        return result