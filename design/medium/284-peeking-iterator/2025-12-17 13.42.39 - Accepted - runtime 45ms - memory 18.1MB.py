"""
LeetCode: 2025 12 17 13.42.39 Accepted Runtime 45ms Memory 18.1MB

Algorithm:
Use a recursive helper function to explore all possibilities.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator

        # Preload the first element if it exists
        if self.iterator.hasNext():
            self._next = self.iterator.next()
        else:
            self._next = None

    def peek(self):
        # Return the cached next value
        return self._next

    def next(self):
        # Return the current next value
        result = self._next

        # Advance the iterator and update the cache
        if self.iterator.hasNext():
            self._next = self.iterator.next()
        else:
            self._next = None

        return result

    def hasNext(self):
        # If we have a cached value, there's a next element
        return self._next is not None
