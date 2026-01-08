"""
LeetCode: 2025 12 21 14.05.27 Accepted Runtime 543ms Memory 42.3MB

Algorithm:
2D dynamic programming: dp[i][j] represents LCS length of text1[0:i] and text2[0:j]. If text1[i-1] == text2[j-1], dp[i][j] = dp[i-1][j-1] + 1 (extend LCS). Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (take best from skipping one character in either string). Return dp[m][n].

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1): 
            for j in range(1, n + 1):

                # if theres a match 
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # if theres no match
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]