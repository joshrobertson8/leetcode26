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