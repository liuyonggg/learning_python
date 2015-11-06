'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.  
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Ref:
    def maxProduct(self, A):
        if (len(A) == 0):
            return 0;

        maxherepre = A[0];
        minherepre = A[0];
        maxsofar = A[0];
        maxhere = 0
        minhere = 0

        for i in xrange(1, len(A)):
            maxhere = max(max(maxherepre * A[i], minherepre * A[i]), A[i]);
            minhere = min(min(maxherepre * A[i], minherepre * A[i]), A[i]);
            maxsofar = max(maxhere, maxsofar);
            maxherepre = maxhere;
            minherepre = minhere;
        return maxsofar;

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxProduct = 0
        if len(A) == 0:
            maxProduct = 0
        else:
            minProduct = A[0]
            maxProduct = A[0]
            tMax = A[0]
            tMin = A[0]
            for i in xrange(1, len(A)):
                t1 = max(A[i], tMax*A[i], tMin*A[i])
                t2 = min(A[i], tMax*A[i], tMin*A[i])
                tMax = t1
                tMin = t2
                maxProduct = max(tMax, maxProduct)
        print ('%d == %d ' % (Ref().maxProduct(A), maxProduct))
        assert (Ref().maxProduct(A) == maxProduct)
        return maxProduct

if __name__ == "__main__":
    s = Solution()
    assert (s.maxProduct([]) == 0)
    assert (s.maxProduct([13]) == 13)

    assert (s.maxProduct([2, 3, -2, 4]) == 6)
    assert (s.maxProduct([2, 3, -2, -4]) == 48)
    assert (s.maxProduct([2, 3, 2, 4]) == 48)
    assert (s.maxProduct([-2, 3, 2, -4]) == 48)

    assert (s.maxProduct([2, -3, 2, 4]) == 8)
    assert (s.maxProduct([-2, -3, 2, -4]) == 24)

