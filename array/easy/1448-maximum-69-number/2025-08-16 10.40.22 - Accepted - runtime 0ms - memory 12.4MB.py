"""
LeetCode: 2025 08 16 10.40.22 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Iterate through each element with its index.

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