'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def __init__(self, matrix=None):
        if not matrix:
            return
        v =  []
        self.positionTable = {}
        for r in xrange(len(matrix)):
            for c in xrange(len(matrix[0])):
                v.append(matrix[r][c])
                self.positionTable[matrix[r][c]] = (r, c)
        self.v = sorted(v)
    def searchMatrix(self, matrix, target):
        # firstly find the right row
        for i in xrange(len(matrix)):
            if matrix[i][-1] >= target:
                break
        for j in reversed(xrange(len(matrix[i]))):
            if matrix[i][j] <= target:
                break
        return (i, j) if matrix[i][j] == target else None
    def searchMatrixConnerCore(self, matrix, i1, j1, i2, j2, target):
        res = []
        for i in xrange(i1, i2+1):
            for j in xrange(j1, j2+1):
                if matrix[i][j] == target:
                    res.append((i, j))
        return res

    def searchMatrixConner(self, matrix, target):
        return self.searchMatrixConnerCore(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, target)

    def searchMatrixConner2Rec(self, matrix, i1, j1, i2, j2, target):
        if (i1 > i2):
            print (m, i1, j1, i2, j2, target)
        assert (i1 <= i2)
        assert (j1 <= j2)
        res = []
        i_new = (i1+i2)/2
        j_new = (j1+j2)/2
        if ((i_new, j_new) == (i1, j1) or (i_new, j_new) == (i2, j2)):
            r = self.searchMatrixConnerCore(matrix, i1, j1, i2, j2, target)
            res = res + r if r else res
        else:
            # it's a matrix
            if (target >= matrix[i1][j1] and target <= matrix[i2][j2]):
                pv = [((i1, j1), (i_new, j_new))]
                if j_new+1 <= j2:
                    pv.append(((i1, j_new+1), (i_new, j2)))
                if i_new+1 <= i2:
                    pv.append(((i_new+1, j1), (i2, j_new)))
                if i_new+1 <= i2 and j_new+1 <= j2:
                    pv.append(((i_new+1, j_new+1), (i2, j2)))
                for (p1, p2) in pv:
                    r = self.searchMatrixConner2Rec(matrix, p1[0], p1[1], p2[0], p2[1], target)
                    res = res + r if r else res
        return res

    def searchMatrixConner2(self, matrix, target):
        return self.searchMatrixConner2Rec(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, target)

    def searchMatrixConner3(self, matrix, target):
        ## search from top-right point
        i = 0
        j = len(matrix[0])-1
        direction = 0 # 0: down, 1: left
        res = []
        while j >= 0 and i < len(matrix):
            if target == matrix[i][j]:
                res.append((i, j))
            elif target > matrix[i][j]:
                direction = 0
            else:
                assert(target < matrix[i][j])
                direction = 1
            if direction == 0:
                i = i + 1
            else:
                assert (direction == 1)
                j = j - 1
        return res


    def searchMatrixConner4Row(self, matrix, col, h, l, target):
        assert (h <= l)
        if h == l:
            #assert matrix[h][col] >= target
            if matrix[h][col] == target:
                return [(h, col)]
            elif matrix[h][col] < target:
                return None
            else:
                assert matrix[h][col] > target
                return self.searchMatrixConner4Col(matrix, h, 0, col, target)
        else:
            r_new = (h+l)/2
            if matrix[r_new][col] > target:
                return self.searchMatrixConner4Row(matrix, col, h, r_new, target)
            elif matrix[r_new][col] < target:
                return self.searchMatrixConner4Row(matrix, col, r_new+1, l, target)
            else:
                assert matrix[r_new][col] == target
                return [(r_new, col)]

    def searchMatrixConner4Col(self, matrix, row, h, l, target):
        assert (h <= l)
        if h == l:
            if matrix[row][h] == target:
                return [(row, h)]
            elif matrix[row][h] > target:
                return None
            else:
                assert matrix[row][h] < target
                return self.searchMatrixConner4Row(matrix, h, row, len(matrix)-1, target)
        else:
            #print ("in searchMatrixConner4Col: ", h, l)
            r_new = (h+l-1)/2 + 1
            if matrix[row][r_new] > target:
                return self.searchMatrixConner4Col(matrix, row, h, r_new-1, target)
            elif matrix[row][r_new] < target:
                return self.searchMatrixConner4Col(matrix, row, r_new, l, target)
            else:
                assert matrix[row][r_new] == target
                return [(row, r_new)]

    def searchMatrixConner4(self, matrix, target):
        if matrix[0][-1] > target:
            return self.searchMatrixConner4Col(matrix, 0, 0, len(matrix[0])-1, target)
        else:
            assert matrix[0][-1] <= target
            return self.searchMatrixConner4Row(matrix, len(matrix[0])-1, 0, len(matrix)-1, target)

    def searchMatrixConner5Rec(self, l, r, target):
        assert (r >= l)
        r_new = (l + r)/2
        if self.v[r_new] == target:
            return [self.positionTable[self.v[r_new]]]
        if l == r:
            return None
        elif self.v[r_new] > target:
            if r_new != l:
                return self.searchMatrixConner5Rec(l, r_new-1, target)
        else:
            assert (self.v[r_new] < target)
            return self.searchMatrixConner5Rec(r_new+1, r, target)


    
    def searchMatrixConner5(self, matrix, target):
        assert (self.v)
        assert (self.positionTable)
        return self.searchMatrixConner5Rec(0, len(self.v)-1, target)
        
        
        
def test_1(m):
    for r in xrange(len(m)):
        for c in xrange(len(m[0])):
            assert Solution().searchMatrixConner(m, m[r][c]) == [(r, c)]
    assert not Solution().searchMatrixConner(m, -1)


def test_2(m):
    for r in xrange(len(m)):
        for c in xrange(len(m[0])):
            assert Solution().searchMatrixConner2(m, m[r][c]) == [(r, c)]
    assert not Solution().searchMatrixConner2(m, -1)

def test_3(m):
    for r in xrange(len(m)):
        for c in xrange(len(m[0])):
            assert Solution().searchMatrixConner3(m, m[r][c]) == [(r, c)]
    assert not Solution().searchMatrixConner3(m, -1)


def test_4(m):
    for r in xrange(len(m)):
        for c in xrange(len(m[0])):
            assert Solution().searchMatrixConner4(m, m[r][c]) == [(r, c)]
    assert not Solution().searchMatrixConner4(m, -1)


def test_5(m):
    s = Solution(m)
    for r in xrange(len(m)):
        for c in xrange(len(m[0])):
            assert s.searchMatrixConner5(m, m[r][c]) == [(r, c)]
    assert not s.searchMatrixConner5(m, -1)

def create(r, c):
    res = []
    n = 0
    for i in xrange(r):
        res.append(range(n, n+c+1))
        n = n + c + 1
    return res

import timeit
if __name__ == '__main__':
    m = [ [1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ] 
    m = create(2000, 300)
    #print timeit.timeit('test_1(m)', setup="from __main__ import test_1, m", number=1)
    #print timeit.timeit('test_2(m)', setup="from __main__ import test_2, m", number=1)
    #print timeit.timeit('test_3(m)', setup="from __main__ import test_3, m", number=1)
    print timeit.timeit('test_4(m)', setup="from __main__ import test_4, m", number=1)
    print timeit.timeit('test_5(m)', setup="from __main__ import test_5, m", number=1)
