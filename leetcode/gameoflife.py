'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

class cell:
    def __init__(self, live):
        self.x = live
        self.nt = 0
    def update(self):
        self.x = int((self.x and (self.nt == 2 or self.nt == 3)) or (not self.x and self.nt == 3))
        self.nt = 0
    def next(self, nbs):
        self.nt = sum([a.x for a in nbs])
    def __str__(self):
        return "%s" % self.x
    def __repr__(self):
        return self.__str__()


class board:
    def __init__(self, iv):
        assert (len(iv) > 0)
        assert (len(iv[0]) > 0)
        self.b = [[ cell(iv[x][y]) for y in xrange(len(iv[0]))] for x in xrange(len(iv)) ]
        self.dummyCell = cell(0)
        self.neighboridx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def update(self):
        [ self.b[x][y].update() for x in xrange(len(self.b)) for y in xrange(len(self.b[0]))]

    def next(self):
        [ self.b[x][y].next(self.getNbs(x, y)) for x in xrange(len(self.b)) for y in xrange(len(self.b[0]))]

    def getNbs(self, x, y):
        return [self.b[x+i][y+j] if (x+i >= 0 and x+i < len(self.b)) and (y+j >= 0 and y+j < len(self.b[0])) else self.dummyCell for (i, j) in self.neighboridx]
        
    def __str__(self):
        res = ""
        for i in xrange(len(self.b)):
            res = res + "%s\n" % self.b[i]
        return res

if __name__ == "__main__":
    b = board([
              [0, 1, 0, 1, 0, 1], 
              [1, 1, 0, 1, 0, 0], 
              [0, 0, 1, 1, 1, 0], 
              [1, 1, 0, 0, 1, 0], 
              [0, 1, 1, 0, 1, 1],
              [1, 0, 1, 1, 0, 0]
             ])
    for i in xrange(1, 10):
        print ("round %d" % i)
        print (b)
        print ()
        b.next()
        b.update()
