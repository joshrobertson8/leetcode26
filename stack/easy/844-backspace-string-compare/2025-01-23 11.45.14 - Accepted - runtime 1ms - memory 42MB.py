"""
LeetCode: 2025 01 23 11.45.14 Accepted Runtime 1ms Memory 42MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public boolean backspaceCompare(String s, String t) {
        return processString(s).equals(processString(t));
    }

    private String processString(String str) {
        StringBuilder result = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c != '#') {
                result.append(c);
            } else {
                if (result.length() > 0) {
                    result.deleteCharAt(result.length() - 1);
                }
            }
        }
        return result.toString();
    }
}
