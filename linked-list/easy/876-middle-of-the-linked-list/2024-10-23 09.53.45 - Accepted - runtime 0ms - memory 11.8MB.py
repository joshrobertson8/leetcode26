"""
LeetCode: 2024 10 23 09.53.45 Accepted Runtime 0ms Memory 11.8MB

Algorithm:
Floyd's cycle detection (tortoise and hare): use slow and fast pointers both starting at head. Move slow one step, fast two steps. When fast reaches end, slow is at middle. For even length, slow points to second middle node.

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