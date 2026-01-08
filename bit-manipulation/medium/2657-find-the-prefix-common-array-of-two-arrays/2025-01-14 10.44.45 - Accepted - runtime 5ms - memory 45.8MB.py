"""
LeetCode: 2025 01 14 10.44.45 Accepted Runtime 5ms Memory 45.8MB

Algorithm:
Maintain two sets tracking elements seen so far in A and B. For each index i, if A[i] equals B[i], increment count. Otherwise, add A[i] to a_vals and B[i] to b_vals. If A[i] is already in b_vals, increment count. If B[i] is already in a_vals, increment count. Store count at each position in result array. This counts common elements up to each prefix.

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


