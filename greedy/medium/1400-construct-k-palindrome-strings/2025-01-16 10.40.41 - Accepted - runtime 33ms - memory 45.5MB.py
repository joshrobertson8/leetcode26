"""
LeetCode: 2025 01 16 10.40.41 Accepted Runtime 33ms Memory 45.5MB

Algorithm:
Count character frequencies using HashMap. A palindrome can have at most one character with odd frequency. Count how many characters have odd frequencies (odd_freq). To form k palindromes, we need at least k characters (s.length() >= k) and at most k characters with odd frequencies (odd_freq <= k). Return true if both conditions hold.

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

