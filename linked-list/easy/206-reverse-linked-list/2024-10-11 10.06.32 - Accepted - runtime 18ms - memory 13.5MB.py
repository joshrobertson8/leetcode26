"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

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