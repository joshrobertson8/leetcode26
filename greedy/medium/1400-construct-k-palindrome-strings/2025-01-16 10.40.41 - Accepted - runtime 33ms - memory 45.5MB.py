"""
LeetCode: 2025 01 16 10.40.41 Accepted Runtime 33ms Memory 45.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public boolean canConstruct(String s, int k) {
        if (s.length() < k) {
            return false;
        }

        HashMap<Character, Integer> freq = new HashMap<>();

        for ( char c : s.toCharArray()) {
            if (freq.containsKey(c)) {
                freq.put(c, freq.get(c) + 1);
            }
            else {
                freq.put(c, 1);
            }

        }
        int odd_freq = 0;

        for (int value : freq.values()) {
            if (value % 2 != 0) {
                odd_freq++;
            }
        }
        if (odd_freq > k) {
            return false;
        }
        return true;

    }
}

