"""
LeetCode: 2025 12 16 14.21.50 Accepted Runtime 0ms Memory 18.4MB

Algorithm:
Iterative reversal: maintain prev (None initially) and current (head). For each node, save next node, point current.next to prev, move prev to current, move current to next. After loop, prev is the new head (last node processed).

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev