"""
LeetCode: 2025 09 26 16.54.10 Accepted Runtime 0ms Memory 14.6MB

Algorithm:
Iterate until condition is met.

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

            

            

