"""
LeetCode: 2026 01 01 14.43.03 Accepted Runtime 233ms Memory 49.8MB

Algorithm:
Use two pointers moving toward each other.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = 0
        # For each index, store a list of [snap_id, value]
        self.snapHistory = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        # Record the value change at the current snapshot id
        self.snapHistory[index].append([self.snapId, val])

    def snap(self) -> int:
        # Take a snapshot and advance the snapshot id
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        records = self.snapHistory[index]

        low, high = 0, len(records) - 1
        res = 0 

        while low <= high:
            mid = (low + high) // 2

            if records[mid][0] <= snap_id:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return records[res][1]
