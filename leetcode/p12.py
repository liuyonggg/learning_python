'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for x in A:
            twos = twos | (ones & x)
            ones = ones ^ x
            commons_mask = ~(ones & twos)
            ones = ones & commons_mask
            twos = twos & commons_mask
        return ones

if __name__ == '__main__':
    r = [3, 2, 3, 3]
    assert (Solution().singleNumber(r)  == 2)
    r = [3, 7, 3, 3, 1, 7, 7]
    assert (Solution().singleNumber(r)  == 1)
