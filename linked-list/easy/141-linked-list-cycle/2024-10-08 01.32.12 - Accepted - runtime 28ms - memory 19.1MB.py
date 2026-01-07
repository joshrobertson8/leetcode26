"""
LeetCode: 2024 10 08 01.32.12 Accepted Runtime 28ms Memory 19.1mb

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, x):
self.val = x
self.next = None

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def hasCycle(self, head):
        current = head
        if not current:
            return False
        seen = set()

        while current and current.next:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False