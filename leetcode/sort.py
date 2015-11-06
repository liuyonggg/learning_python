class Solution:
    def Sort(self,nums):
        num = []
        for i in xrange(len(nums)):
            minf = min(nums)
            num.append(minf)
            nums.remove(minf)
        return num

print Solution().Sort([1,2,4,5,3,2,178,53,7,9,98,7,87,56,6,5,64,355,7,8,67,8])
