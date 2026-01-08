"""
LeetCode: 2024 10 10 01.53.30 Accepted Runtime 43ms Memory 18.4MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        
        dummy = ListNode()
        dummy.next = head
        current = head
        prev = dummy

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next