'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = 0
        for x in A:
            r = r ^ x
        return r
        

if __name__ == '__main__':
    a = [3, 3, 2]
    assert (Solution().singleNumber(a) == 2)

    a = [3, 3, 2, 2, 7]
    assert (Solution().singleNumber(a) == 7)

        
