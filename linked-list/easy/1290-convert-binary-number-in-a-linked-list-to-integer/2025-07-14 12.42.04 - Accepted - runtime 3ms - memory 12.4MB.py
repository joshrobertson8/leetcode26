"""
LeetCode: 2025 07 14 12.42.04 Accepted Runtime 3ms Memory 12.4MB

Algorithm:
Traverse the linked list.

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
            result = result * 2 + current.val
            current = current.next
        return result