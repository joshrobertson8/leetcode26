"""
LeetCode: 2025 01 23 11.45.14 Accepted Runtime 1ms Memory 42MB

Algorithm:
Process strings using StringBuilder: for each character, if it's '#', delete last character if StringBuilder is not empty. Otherwise append character. Process both strings and compare results. This simulates backspace behavior and compares final strings.

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
