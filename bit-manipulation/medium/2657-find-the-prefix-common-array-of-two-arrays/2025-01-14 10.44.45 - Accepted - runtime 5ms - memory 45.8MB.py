"""
LeetCode: 2025 01 14 10.44.45 Accepted Runtime 5ms Memory 45.8MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] result = new int[n];
        int count = 0; 

        Set<Integer> a_vals = new HashSet<>();
        Set<Integer> b_vals = new HashSet<>();

        for (int i = 0; i < A.length; i++) {
            
            if (A[i] == B[i]) {
                count += 1;
            }
            else {
                a_vals.add(A[i]);
                b_vals.add(B[i]);

                if (b_vals.contains(A[i])) {
                    count += 1;
                }
                if (a_vals.contains(B[i])) {
                    count += 1;
                }
            }
        result[i] = count;
        }
    return result;
    }
}


