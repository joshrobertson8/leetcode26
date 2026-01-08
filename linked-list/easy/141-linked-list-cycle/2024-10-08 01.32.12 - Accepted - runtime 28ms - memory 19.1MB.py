"""
LeetCode: 2024 10 08 01.32.12 Accepted Runtime 28ms Memory 19.1MB

Algorithm:
Use set to track visited nodes. Traverse list, if current node is in set, cycle detected (return True). Otherwise add to set and continue. If we reach end (current is None), no cycle (return False).

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        current = head
        if not current:
            return False
        seen = set()

        while current and current.next:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False

        
        
