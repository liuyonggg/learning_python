'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self,nums):
        num = []
        for i in xrange(len(nums)):
            x = 1
            for j in xrange(len(nums)):
                x = x * nums[j] if j != i else x
            num.append(x)
        return num



assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
