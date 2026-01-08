"""
LeetCode: 2025 12 26 18.40.47 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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