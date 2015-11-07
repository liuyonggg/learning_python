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

def test_1(v, refv):
    assert (Solution().sort(v) == refv)


def test_2(v, refv):
    assert (Solution().bubbleSort(v) == refv)
    
if __name__ == "__main__":
    random.seed(0)
    refm = range(10000)
    #refm = range(10)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    
    print timeit.timeit(stmt='assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_2(m, refm)', setup="from __main__ import test_2, m, refm", number=1)
