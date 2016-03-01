from pyeda.inter import *

X = exprvars('x', (1,1000))

class Solve:
    def __init__(self):
        cycle = 0
        bound = 10

        self.T1 = And(X[cycle*bound+1], X[(cycle+1)*bound+2])
        cycle += 1

        self.T2 = And(X[cycle*bound+2], And(X[(cycle+1)*bound+1], X[(cycle+1)*bound+3]))
        cycle += 1

        self.I = X[1]
        self.clauses = And(self.I, self.T1, self.T2)

        self.F = [X[3], X[bound+3], X[2*bound+3]]

    def solve(self):
        res = []
        for i in range(0, 3):
            S = And(self.clauses, Not(self.F[i]))
            S = S.to_cnf()
            if not S.satisfy_one():
                res.append(self.F[i])
        if not res:
            print ("no solution")
            return

        for s in res:
            S = And(self.clauses, s)
            S = S.to_cnf()
            print (S.satisfy_one())
        return


if __name__ == "__main__":
    s = Solve()
    s.solve()

