class permutation:
    def __init__(self, v):
        self.v = v
    def __iter__(self):
        return self
    def next(self):
        return self.permutationRec(self.v)
    def permutationRec(self, candidates):
        if len(candidates) == 1:
            return [[candidates[0]]]
        v = []
        for i in xrange(len(candidates)):
            nc = [candidates[x] for x in xrange(len(candidates)) if x != i]
            v += [ [candidates[i]]+x for x in self.permutationRec(nc)]
        return v

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print "cycles=%s indices=%s" % (cycles, indices)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        print "n > 0, cycles=%s indices=%s" % (cycles, indices)
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
                print "i=%d cycles=%s indices=%s" % (i, cycles, indices)
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print "i=%d cycles=%s indices=%s" % (i, cycles, indices)
                yield tuple(pool[i] for i in indices[:r])
                print "after yield"
                break
        else:
            print "before return"
            return

if __name__ == "__main__":
    assert (permutation([0, 1, 2, 3]).next()) == ([[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]])


    for x in permutations([0, 1, 2]):
        print x
