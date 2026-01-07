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
    def isPalindrome(self, head):
        current = head
        arr = []

        while current:
            arr.append(current.val)
            current = current.next
        
        r_arr = arr[::-1]

        if r_arr == arr:
            return True
        return False