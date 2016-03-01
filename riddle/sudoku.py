from pyeda.inter import *

X = exprvars('x', (1,10), (1,10), (1,10))
class Solve:
    def __init__(self):
        self.DIGITS = "123456789"
        self.F = And (*[ And (*[ OneHot (*[X[r,c,v] for v in range(1,10)]) for c in range(1,10)]) for r in range(1,10)])
        self.C = And (*[ And (*[ OneHot (*[X[r,c,v] for r in range(1,10)]) for v in range(1,10)]) for c in range(1,10)])
        self.R = And (*[ And (*[ OneHot (*[X[r,c,v] for c in range(1,10)]) for v in range(1,10)]) for r in range(1,10)])
        self.box = And (*[ And (*[ And (*[ OneHot (*[X[r,c,v] for r in range(i*3+1,(i+1)*3+1) for c in range(j*3+1,(j+1)*3+1)]) for v in range(1,10)]) for i in range(0, 3)]) for j in range(0, 3)])

    def solve(self, grid=True):
        S = And(self.F, self.C, self.R, self.box, grid)
        S = S.to_cnf()
        return S.satisfy_one()

    def toGrid(self, gridStr):
        grid = True
        assert (len(gridStr) == 81)
        r = 0
        c = 0
        for ch in gridStr:
            assert (ch in self.DIGITS or ch in ".")
            if ch in self.DIGITS:
                grid = And (grid, X[r+1, c+1, int(ch)])
            r = r + (c == 8)
            c = (c + 1) % 9
        return grid

    def display(self, solutions):
        for s in solutions:
            self.display(s)
            print ("\n\n")

    def displayOne(self, solution):
        for r in range(1,10):
            line = ""
            for c in range(1,10):
                for v in range(1,10):
                    if solution[X[r, c, v]]:
                        line = line + ("%d " % v)
            print ("%s" % line)

if __name__ == "__main__":
    gridStr = (
".73...8.."
"..413..5."
".85..631."
"5...9..3."
"..8.1.5.."
".1..6...7"
".516..28."
".4..529.."
"..2...64.")

    s = Solve()
    #print (s.solve(s.toGrid(gridStr)))
    #s.displayOne(s.solve(s.toGrid(gridStr)))
    s.displayOne(s.solve())

