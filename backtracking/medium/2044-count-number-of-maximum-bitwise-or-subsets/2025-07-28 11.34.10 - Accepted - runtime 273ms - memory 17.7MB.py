"""
LeetCode: 2025 07 28 11.34.10 Accepted Runtime 273ms Memory 17.7MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maxOr = 0
        count = 0

        # Step 1: Find the maximum OR possible
        for num in nums:
            maxOr |= num

        # Step 2: Sort to allow pruning (optional but sometimes helps)
        nums.sort(reverse=True)

        # Step 3: Backtracking with pruning
        def backtrack(idx, curOr):
            nonlocal count

            # Prune if current OR can't possibly reach maxOr
            if curOr | maxOr != maxOr:
                return

            # Base case: finished all decisions
            if idx == n:
                if curOr == maxOr:
                    count += 1
                return

            # Include nums[idx]
            backtrack(idx + 1, curOr | nums[idx])

            # Exclude nums[idx]
            backtrack(idx + 1, curOr)

        backtrack(0, 0)
        return count