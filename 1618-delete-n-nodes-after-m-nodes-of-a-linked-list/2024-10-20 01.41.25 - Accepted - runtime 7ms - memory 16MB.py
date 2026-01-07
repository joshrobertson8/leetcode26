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
    def deleteNodes(self, head, m, n):
        current = head
        prev = head

        while current:
            # Traverse m nodes
            mcount = m
            while current and mcount > 0:
                prev = current
                current = current.next
                mcount -= 1

            # Traverse and delete n nodes
            ncount = n
            while current and ncount > 0:
                current = current.next
                ncount -= 1

            # Link the last m-th node to the node after skipping n nodes
            prev.next = current
        
        return head