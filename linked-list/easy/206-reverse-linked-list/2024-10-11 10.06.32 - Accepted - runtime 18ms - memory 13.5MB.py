"""
LeetCode: 2024 10 11 10.06.32 Accepted Runtime 18ms Memory 13.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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

        