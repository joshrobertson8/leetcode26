"""
LeetCode: 2025 09 18 12.06.10 Accepted Runtime 789ms Memory 110.9MB

Algorithm:
Use a min-heap (priority queue) with negative priorities for max-heap behavior, and a hash map to track current task states. add() and edit() update the map and push to heap. rmv() removes from map only. execTop() pops from heap until finding a valid task (exists in map and priority matches current state), then removes it. This handles stale heap entries lazily.

Time Complexity: O(n) for add/edit/execTop, O(1) for rmv
Space Complexity: O(1)
"""

import heapq

class TaskManager:
    def __init__(self, tasks):
        self.task_map = {}   # taskId -> (userId, priority)
        self.heap = []       # [(-priority, -taskId, taskId)]
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self):
        while self.heap:
            negP, negT, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                userId, curP = self.task_map[taskId]
                if curP == -negP:
                    del self.task_map[taskId]
                    return userId
        return -1
