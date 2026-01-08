"""
LeetCode: 2025 06 13 13.58.46 Accepted Runtime 2ms Memory 42MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public int lengthOfLastWord(String s) {
        String clean = s.trim();
        int count = 0;

        for (int i = 0; i < clean.length(); i++) {
            if (clean.charAt(i) == ' ') {
                count = 0;
            } else {
                count += 1;
            }
        }
        return count;
    }
}