'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''
import heapq

class Solution():
    def __init__(self):
        self.uglyNumberTable = [1]
    def isUglyNumber(self, uglyNumberCadidate):
        if uglyNumberCadidate == 1:
            return True
        n = uglyNumberCadidate
        for d in [2, 3, 5]:
            while n % d == 0:
                n = n / d
            if n == 1:
                return True
        return False
        
    def nthUglyNumberConner(self, n):
        i = 0
        uglyNumberCadidate = 0
        while i < n:
            uglyNumberCadidate += 1
            if self.isUglyNumber(uglyNumberCadidate):
                i += 1 
        assert (i == n)
        assert (self.isUglyNumber(uglyNumberCadidate))
        return uglyNumberCadidate

    def nthUglyNumberConnerPlus(self, n):
        """
        :type n: int want find n ugly number
        :rtype: int ugly number
        """
        if n <= len(self.uglyNumberTable):
            return self.uglyNumberTable[n-1]
        i = len(self.uglyNumberTable)
        uglyNumberCadidate = self.uglyNumberTable[-1] 
        while i < n:
            uglyNumberCadidate += 1
            if self.isUglyNumber(uglyNumberCadidate):
                self.uglyNumberTable.append(uglyNumberCadidate)
                i += 1 
        assert (i == n)
        assert (self.isUglyNumber(uglyNumberCadidate))
        return uglyNumberCadidate

    def nthUglyNumberConner3(self, n):
        """
        :type n: int want find n ugly number
        :rtype: int ugly number
        """
        v = [1]
        while len(v) < 2*n:
            v2 = [ x * 2 for x in v]
            v3 = [ x * 3 for x in v]
            v4 = [ x * 4 for x in v]
            v5 = [ x * 5 for x in v]
            y = 0
            vt = []
            for x in heapq.merge(v, v2, v3, v4, v5):
                if y != x:
                    vt.append(x)
                    y = x
            v = vt
        assert (len(v) >= n)
        return v[n-1]


    def nthUglyNumberConner4(self, n):
        """
        :type n: int want find n ugly number
        :rtype: int ugly number
        """
        v = [1]
        p = [0, 0, 0]
        pv = [2, 3, 5]
        while len(v) < n:
            m = [ v[p[i]] * pv[i] for i in xrange(len(p))]
            mm = min(m)
            for i in xrange(len(p)):
                if m[i] == mm:
                    p[i] += 1
            v.append(mm)
        assert (len(v) == n)
        return v[n-1]
        
    def nthUglyNumber(self, n):
        """
        for any ugly number N, 
            if N is >  3, N could be expressed as 2^^k * b, where b is 2**2, 5 or 2*3
            if N is <= 3, N could be 1, 2, 3 
        :type n: int
        :rtype: int
        """
        assert (n > 0)
        if n <= 3:
            return [1,2,3][n-1]
        k = (n - 3 - 1)/ 3
        b = (n-1) % 3
        return 2**k * [2**2, 5, 2*3][b]
        

if __name__ == "__main__":
    v = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25]
    for i in xrange(len(v)):
        assert Solution().nthUglyNumberConner(i+1) == v[i]
        assert Solution().nthUglyNumberConnerPlus(i+1) == v[i]

    '''
    s2 = Solution()
    s2.nthUglyNumberConnerPlus(27)
    print s2.uglyNumberTable
    '''
    #print Solution().nthUglyNumberConner4(27)
    #print Solution().nthUglyNumberConner3(1000000)

    print Solution().nthUglyNumberConner4(100000000)

    #print Solution().nthUglyNumberConner(1000)
    #Solution().nthUglyNumberConner(1000)
    #s2 = Solution()
    #s2.nthUglyNumberConnerPlus(1000)
    #s2.nthUglyNumberConnerPlus(1000)
    #print Solution().nthUglyNumberConnerPlus(1000)
