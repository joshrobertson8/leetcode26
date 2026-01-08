"""
LeetCode: 2024 10 11 10.06.32 Accepted Runtime 18ms Memory 13.5MB

Algorithm:
Iterative reversal: handle empty list first. Maintain prev (None initially) and current (head). For each node, save next node, point current.next to prev, move prev to current, move current to next. After loop, prev is the new head.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None

        if not head:
            return None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

        