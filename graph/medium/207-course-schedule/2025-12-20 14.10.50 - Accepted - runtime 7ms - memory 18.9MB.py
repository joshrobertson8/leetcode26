"""
LeetCode: 2025 12 20 14.10.50 Accepted Runtime 7ms Memory 18.9MB

Algorithm:
Use a set for O(1) lookup. Use a recursive helper function to explore all possibilities.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # adj list for Top Sort
        graph = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites: 
            graph[crs].append(pre)

        
        visited = set()
        cycle = set()

        def dfs(course):

            if course in visited: 
                return True

            if course in cycle: 
                return False

            cycle.add(course)

            for pre in graph[course]: 
                if dfs(pre) == False: 
                    return False

            cycle.remove(course)
            visited.add(course)
            return True

        for crs in range(numCourses): 
            if dfs(crs) == False: 
                return False
        return True
