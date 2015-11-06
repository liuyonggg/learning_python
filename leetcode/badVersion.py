'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def __init__(self, v):
        self.v = v 
    def isBadVersion(self, n):
        return self.v[n]
    def findBadVersion(self, l, r):
        assert (r >= l + 1)
        assert (not self.isBadVersion(l))
        assert (self.isBadVersion(r))
        if (l + 1 == r):
            return r
        nr = (l+r-1)/2+1
        if self.isBadVersion(nr):
            return self.findBadVersion(l, nr)
        else:
            return self.findBadVersion(nr, r)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isBadVersion(1):
            return 1
        elif self.isBadVersion(n):
            return self.findBadVersion(1, n)
        else:
            return -1

if __name__ == "__main__":
    v = [-1, 0, 0, 0, 1, 1, 1, 1]
    s = Solution(v)
    assert s.firstBadVersion(len(v)-1) == 4

    v = [-1, 0, 0, 1, 1, 1, 1, 1]
    s = Solution(v)
    assert s.firstBadVersion(len(v)-1) == 3

    v = [-1, 0, 0, 1, 1, 1, 1, 1, 1]
    s = Solution(v)
    assert s.firstBadVersion(len(v)-1) == 3
    
    v = [-1, 0, 1, 1, 1, 1, 1, 1, 1]
    s = Solution(v)
    assert s.firstBadVersion(len(v)-1) == 2

    v = [-1, 0, 1, 1, 1, 1, 1, 1]
    s = Solution(v)
    assert s.firstBadVersion(len(v)-1) == 2
