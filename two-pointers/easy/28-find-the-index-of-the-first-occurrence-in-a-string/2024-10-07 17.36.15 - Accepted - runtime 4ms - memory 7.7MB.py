"""
LeetCode: 2024 10 07 17.36.15 Accepted Runtime 4ms Memory 7.7MB

Algorithm:
Brute force string matching: for each starting position i in haystack (0 to len_haystack - len_needle), check if needle matches substring starting at i. Compare character by character. If all characters match (j == len_needle), return i. If no match found, return -1. This finds first occurrence of needle in haystack.

Time Complexity: O(?)
Space Complexity: O(?)
"""

int strStr(char* haystack, char* needle) {
    int len_haystack = strlen(haystack);
    int len_needle = strlen(needle);
    
    if (len_needle == 0) {
        return 0;
    }

    for (int i = 0; i <= len_haystack - len_needle; i++) {
        int j;
        for (j = 0; j < len_needle; j++) {
            if (haystack[i + j] != needle[j]) {
                break;
            }
        }
        if (j == len_needle) {
            return i;
        }
    }
    
    return -1;
}
