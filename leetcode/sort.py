import random
import copy
import timeit


class Solution:
    def sort(self,nums):
        vs = copy.deepcopy(nums)
        num = []
        for i in xrange(len(vs)):
            minf = min(vs)
            num.append(minf)
            vs.remove(minf)
        return num

    def bubbleSort(self, nums):
        vs = copy.deepcopy(nums)
        for i in xrange(len(vs)):
            hasBubble = False
            for j in xrange(len(vs)-1-i):
                if vs[j] > vs[j+1]:
                    v = vs[j+1]
                    vs[j+1] = vs[j]
                    vs[j] = v
                    hasBubble = True
            if not hasBubble:
                break
        return vs

    def quickSort(self, nums):
        less = []
        equal = []
        bigger = []
        if not nums:
            return []
        pivot = nums[0]
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                assert (x > pivot)
                bigger.append(x)
        return self.quickSort(less) + equal + self.quickSort(bigger)

def test_1(v, refv):
    assert (Solution().sort(v) == refv)


def test_2(v, refv):
    assert (Solution().bubbleSort(v) == refv)

def test_quicksort(v, refv):
    assert (Solution().quickSort(v) == refv)
    
if __name__ == "__main__":
    random.seed(0)
    refm = range(10000)
    #refm = range(10)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    
    print timeit.timeit(stmt='assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_2(m, refm)', setup="from __main__ import test_2, m, refm", number=1)
    print timeit.timeit(stmt='test_quicksort(m, refm)', setup="from __main__ import test_quicksort, m, refm", number=1)
