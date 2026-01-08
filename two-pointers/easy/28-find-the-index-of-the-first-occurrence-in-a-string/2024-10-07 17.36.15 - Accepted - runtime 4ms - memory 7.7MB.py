"""
LeetCode: 2024 10 07 17.36.15 Accepted Runtime 4ms Memory 7.7MB

Algorithm:
TODO: Describe your approach here

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
