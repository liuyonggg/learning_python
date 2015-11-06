import random
import copy
import timeit


class Solution:
    def sort(self,nums):
        num = []
        for i in xrange(len(nums)):
            minf = min(nums)
            num.append(minf)
            nums.remove(minf)
        return num

def test_1(m, refm):
    assert (Solution().sort(m) == refm)
    
if __name__ == "__main__":
    refm = range(1000)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    
    print timeit.timeit('assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit('test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
