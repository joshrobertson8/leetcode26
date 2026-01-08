"""
LeetCode: 2024 10 23 09.53.45 Accepted Runtime 0ms Memory 11.8MB

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
    def middleNode(self, head):

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow