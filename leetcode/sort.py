import random
import copy
import timeit

def test_1(m, refm):
    pass
    #assert (Solution().sort(m) == refm)
    
if __name__ == "__main__":
    refm = range(100000)
    m = copy.deepcopy(refm)
    random.shuffle(m)
    
    print timeit.timeit('assert sorted(m) == refm', setup="from __main__ import test_1, m, refm", number=1)
    print timeit.timeit('test_1(m, refm)', setup="from __main__ import test_1, m, refm", number=1)
