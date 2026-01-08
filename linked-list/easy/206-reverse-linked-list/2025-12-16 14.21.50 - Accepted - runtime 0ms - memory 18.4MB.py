"""
LeetCode: 2025 12 16 14.21.50 Accepted Runtime 0ms Memory 18.4MB

Algorithm:
Use two pointers moving toward each other.

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