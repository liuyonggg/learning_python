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

    def partition(self, nums, lo, hi):
        assert (lo < hi)
        i = lo
        j = hi
        pv = nums[lo]
        while True:
            while nums[i] < pv:
                i = i + 1
            while nums[j] > pv:
                j = j - 1
            if i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
            else:
                return j
        
    def quickSort2Core(self, nums, lo, hi):
        if lo < hi:
            pi = self.partition(nums, lo, hi)
            self.quickSort2Core(nums, lo, pi-1)
            self.quickSort2Core(nums, pi+1, hi)
                   
    def quickSort2(self, nums):
        self.quickSort2Core(nums, 0, len(nums)-1)
        return nums
        

def test_1(v, refv):
    assert (Solution().sort(v) == refv)


def test_2(v, refv):
    assert (Solution().bubbleSort(v) == refv)

def test_quicksort(v, refv):
    assert (Solution().quickSort(v) == refv)

    
def test_quicksort2(v,refv):
    assert (Solution().quickSort2(v) == refv)

if __name__ == "__main__":
    random.seed(0)
    refm = range(10000)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    #m = [9, 4, 0, 5, 2]
    #refm = [0, 2, 4, 5, 9]
    
    print timeit.timeit(stmt='assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
    #print timeit.timeit(stmt='test_2(m, refm)', setup="from __main__ import test_2, m, refm", number=1)
    print timeit.timeit(stmt='test_quicksort(m, refm)', setup="from __main__ import test_quicksort, m, refm", number=1)
    print timeit.timeit(stmt='test_quicksort2(m, refm)', setup="from __main__ import test_quicksort2, m, refm", number=1)

