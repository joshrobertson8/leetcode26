"""
LeetCode: 2024 11 25 20.41.12 Accepted Runtime 2ms Memory 16.1MB

Algorithm:
Use two pointers moving toward each other.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: Optional[ListNode]
        :type m: int
        :type n: int
        :rtype: Optional[ListNode]
        """
        current = head 
        prev = head

        while current:
            
            mc = m 
            while current and mc > 0:
                prev = current 
                current = current.next
                mc -= 1

            nc = n 
            while current and nc > 0:
                current = current.next
                nc -= 1

            prev.next = current 

        return head

        