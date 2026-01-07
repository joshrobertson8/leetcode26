"""
LeetCode: 2024 10 08 01.54.14 Accepted Runtime 127ms Memory 41.3mb

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
    def getIntersectionNode(self, headA, headB):

        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pB