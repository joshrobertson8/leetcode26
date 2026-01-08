"""
LeetCode: 2025 09 26 16.54.10 Accepted Runtime 0ms Memory 14.6MB

Algorithm:
Iterative reversal: maintain prev (None initially) and current (head). For each node, save next node, point current.next to prev, move prev to current, move current to next. After loop, prev is the new head (last node processed).

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
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        prev = None

        while current: 
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev

            

            

