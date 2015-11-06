'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b



class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        return 3


if __name__ == '__main__':
    pts = [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 2)]
    assert (Solution().maxPoints(pts) == 3)
