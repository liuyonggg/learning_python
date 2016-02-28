from pyeda.inter import *

'''
The Englishman lives in the red house.
The Swede keeps dogs.
The Dane drinks tea.
The green house is just to the left of the white one.
The owner of the green house drinks coffee.
The Pall Mall smoker keeps birds.
The owner of the yellow house smokes Dunhills.
The man in the center house drinks milk.
The Norwegian lives in the first house.
The Blend smoker has a neighbor who keeps cats.
The man who smokes Blue Masters drinks beer.
The man who keeps horses lives next to the Dunhill smoker.
The German smokes Prince.
The Norwegian lives next to the blue house.
The Blend smoker has a neighbor who drinks water.
'''

X = exprvars('x', (1,6), (1,6), (1,6))
class Solve:
    def __init__(self):
        X = exprvars('x', (1,6), (1,6), (1,6))
        self.DIGITS = "123456789"
        self.F = And (*[ And (*[ OneHot (*[X[r,c,v] for v in range(1,6)]) for c in range(1,6)]) for r in range(1,6)])
        self.C = And (*[ And (*[ OneHot (*[X[r,c,v] for r in range(1,6)]) for v in range(1,6)]) for c in range(1,6)])
        # The Englishman lives in the red house.
        self.r1 = Or (*[ And(X[r, 1, 1], X[r, 2, 1]) for r in range(1,6)])
        # The Swede keeps dogs.
        self.r2 = Or (*[ And(X[r, 1, 2], X[r, 3, 1]) for r in range(1,6)])
        # The Dane drinks tea.
        self.r3 = Or (*[ And(X[r, 1, 5], X[r, 4, 1]) for r in range(1,6)])
        # The green house is just to the left of the white one.
        self.r4 = Or (*[ And(X[r, 2, 2], X[r+1, 2, 3]) for r in range(1,5)])
        # The owner of the green house drinks coffee.
        self.r5 = Or (*[ And(X[r, 2, 2], X[r, 4, 2]) for r in range(1,6)])
        # The Pall Mall smoker keeps birds.
        self.r6 = Or (*[ And(X[r, 5, 1], X[r, 3, 2]) for r in range(1,6)])
        # The owner of the yellow house smokes Dunhills.
        self.r7 = Or (*[ And(X[r, 2, 4], X[r, 5, 2]) for r in range(1,6)])
        # The man in the center house drinks milk.
        self.r8 = X[3, 4, 3]
        #The Norwegian lives in the first house.
        self.r9 = X[1, 1, 3]
        #The Blend smoker has a neighbor who keeps cats.
        self.r10 = Or (Or (*[ And(X[r, 5, 3], X[r+1, 3, 2]) for r in range(1,5)]), Or (*[ And(X[r, 5, 3], X[r-1, 3, 2]) for r in range(2,6)]))
        #The man who smokes Blue Masters drinks beer.
        self.r11 = Or (*[ And(X[r, 5, 4], X[r, 4, 4]) for r in range(1,6)])
        #The man who keeps horses lives next to the Dunhill smoker.
        self.r12 = Or (Or (*[ And(X[r, 3, 4], X[r+1, 5, 2]) for r in range(1,5)]), Or (*[ And(X[r, 3, 4], X[r-1, 5, 2]) for r in range(2,6)]))
        #The German smokes Prince.
        self.r13 = Or (*[ And(X[r, 1, 4], X[r, 5, 5]) for r in range(1,6)])
        #The Norwegian lives next to the blue house.
        self.r14 = Or (Or (*[ And(X[r, 1, 3], X[r+1, 2, 5]) for r in range(1,5)]), Or (*[ And(X[r, 1, 3], X[r-1, 2, 5]) for r in range(2,6)]))
        #The Blend smoker has a neighbor who drinks water.
        self.r15 = Or (Or (*[ And(X[r, 5, 3], X[r+1, 4, 5]) for r in range(1,5)]), Or (*[ And(X[r, 5, 3], X[r-1, 4, 5]) for r in range(2,6)]))
        
        

    def solve(self):
        S = And(self.F, self.C, self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15)
        #answer = And(X[1,1,3], X[2,1,5], X[3,1,1], X[4,1,4], X[5,1,2], X[1,2,4], X[2,2,5], X[3,2,1], X[4,2,2], X[5,2,3], X[1,3,3],X[2,3,4], X[3,3,2], X[4,3,5], X[5,3,1], X[1,4,5],X[2,4,1],X[3,4,3],X[4,4,2],X[5,4,4],X[1,5,2],X[2,5,3],X[3,5,1],X[4,5,5],X[5,5,4])
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
        for r in range(1,6):
            line = ""
            for c in range(1,6):
                for v in range(1,6):
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
    print (s.solve())
    #s.displayOne(s.solve(gridStr))

