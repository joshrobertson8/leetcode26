"""
LeetCode: 2025 12 26 18.40.47 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
Two pointers: i scans through array, base tracks write position. For each character group: count consecutive occurrences, write character to chars[base], increment base. If count > 1, write each digit of count as character. Return base (new length). This compresses array in-place by replacing consecutive characters with character and count.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        base = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1

            chars[base] = ch
            base += 1

            if count > 1: 
                for d in str(count):
                    chars[base] = d
                    base += 1
            

        return base