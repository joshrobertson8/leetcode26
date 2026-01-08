"""
LeetCode: 2025 12 16 14.21.50 Accepted Runtime 0ms Memory 18.4MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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