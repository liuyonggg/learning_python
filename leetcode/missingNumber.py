'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

import operator

class Solution():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n+1)*n/2 - sum(nums)

    def missingNumberUsingXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums) ^ reduce(operator.xor, xrange(len(nums)+1))

if __name__ == "__main__":
    assert Solution().missingNumber([0, 1, 2, 3, 5]) == Solution().missingNumberUsingXor([5, 3, 1, 0, 2])
        
