"""
LeetCode: 2025 08 16 10.40.22 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Convert the number to a string and iterate through each digit. When we find the first '6', replace it with '9' and append the rest of the string, then break. If we only see '9's, keep building the result with '9's. This maximizes the number by changing the leftmost 6 to 9.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        strNum = str(num)
        res = ''
        
        for i, j in enumerate(strNum): 

            if j == '6':
                res += '9' + strNum[i + 1:]
                break

            else: 
                res += '9'
            
        return int(res)