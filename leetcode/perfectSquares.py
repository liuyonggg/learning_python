'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
1. the number like 8b+7 could be represented by 3 square numbers
2. all numbers could be represented by 4 square numbers
'''

class Solution(object):
    def numSquares(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        
