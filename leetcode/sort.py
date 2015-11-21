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
        while i < j:
            while nums[i] < pv:
                i = i + 1
            while nums[j] > pv:
                j = j - 1
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            if nums[i] == nums[j] and i < j:
                i = i + 1
        return j
       
    def quickSort2Core(self, nums, lo, hi):
        if lo < hi:
            pi = self.partition(nums, lo, hi)
            self.quickSort2Core(nums, lo, pi-1)
            self.quickSort2Core(nums, pi+1, hi)
                  
    def quickSort2(self, nums):
        self.quickSort2Core(nums, 0, len(nums)-1)
        return nums

    def merge(self, nums1, nums2):
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i = i + 1
            else:
                res.append(nums2[j])
                j = j + 1
        res = res + nums1[i:] if i < len(nums1) else res + nums2[j:]
        return res

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mp = (len(nums)- 1)/2
        l = self.mergeSort(nums[:mp+1])
        r = self.mergeSort(nums[mp+1:])
        return self.merge(l, r)

def test_1(v, refv):
    assert (Solution().sort(v) == refv)


def test_bubbleSort(v, refv):
    assert (Solution().bubbleSort(v) == refv)

def test_quicksort(v, refv):
    assert (Solution().quickSort(v) == refv)

    
def test_quicksort2(v,refv):
    assert (Solution().quickSort2(v) == refv)

def test_merge():
    assert Solution().merge([1, 5, 6], [2, 3, 4]) == [1, 2, 3 ,4, 5, 6]
    assert Solution().merge([1], [2, 3, 4]) == [1, 2, 3 ,4]
    assert Solution().merge([1, 2, 3], [4]) == [1, 2, 3 ,4]
    

def test_mergesort(v,refv):
    assert (Solution().mergeSort(v) == refv)

def test_all_2():
    refm = [0, 1, 1, 1, 1] + range(1, 2000)
    m = copy.deepcopy(refm)
    random.shuffle(m)

    assert sorted(m) == refm
    test_1(m, refm)
    test_bubbleSort(m, refm)
    test_quicksort(m, refm)
    test_quicksort2(m, refm)
    test_mergesort(m, refm)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(100000)
    random.seed(0)
    refm = range(1000, 2000)
    refm = range(100)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    
    print timeit.timeit(stmt='assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=10000)
    print timeit.timeit(stmt='test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit(stmt='test_bubbleSort(m, refm)', setup="from __main__ import test_bubbleSort, m, refm", number=1)
    print timeit.timeit(stmt='test_quicksort(m, refm)', setup="from __main__ import test_quicksort, m, refm", number=1)
    print timeit.timeit(stmt='test_quicksort2(m, refm)', setup="from __main__ import test_quicksort2, m, refm", number=1)
    test_merge()
    print timeit.timeit(stmt='test_mergesort(m, refm)', setup="from __main__ import test_mergesort, m, refm", number=1)

    test_all_2()

