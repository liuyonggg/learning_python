'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
'''

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)):
            if nums[i] == 0:
                j = len(nums)-1
                for j in xrange(i+1, len(nums)):
                    if nums[j] != 0:
                        break
                assert (j > i or i == len(nums)-1)
                assert (j == len(nums)-1 or nums[j] != 0)
                if j < len(nums):
                    nums[i] = nums[j]
                    nums[j] = 0
    def check(self, nums):
        """
        check if all 0 are in end of array
        """
        for i in xrange(len(nums)):
            if nums[i] == 0:
                break
        for j in xrange(i, len(nums)):
            assert nums[j] == 0


if __name__ == "__main__":
    s = Solution()
    a = [1, 0, 0, 2, 3]
    s.moveZeroes(a)
    s.check(a)
