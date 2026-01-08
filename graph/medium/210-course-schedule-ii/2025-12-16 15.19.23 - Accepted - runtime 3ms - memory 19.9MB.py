"""
LeetCode: 2025 12 16 15.19.23 Accepted Runtime 3ms Memory 19.9MB

Algorithm:
Topological sort using DFS: build adjacency list where graph[course] contains prerequisites. Use visited set (completed courses) and cycle set (currently processing). For each course, if in cycle, return False (cycle detected). If visited, return True. Add to cycle, recursively process prerequisites. If all prerequisites complete, remove from cycle, add to visited, append to result. Return result if all courses can be completed.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build adj list of prereqs for DFS
        graph = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites: 
            graph[crs].append(pre)

        res = []
        visited, cycle = set(), set()

        def dfs(course): 
            if course in cycle: 
                return False
            
            if course in visited: 
                return True
    
            cycle.add(course)

            for preReq in graph[course]: 
                if dfs(preReq) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True
        
        for c in range(numCourses):

            if dfs(c) == False: 
                return [] 
            
        return res