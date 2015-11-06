'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''


def getOp(ops, num):
    ops2 = map(tuple, (ops,)) * num
    res = [[]]
    for op in ops2:
        res = [x+[y] for x in res for y in op]
    for op in res:
        yield tuple(op)

class OpIterator():
    '''
    iterate all operator combinations
    '''
    def __init__(self, ops, num):
        self.num = num
        self.ops = []
        self.idx = 0
        ops2 = map(tuple, (ops,)) * self.num
        res = [[]]
        for op in ops2:
            res = [x+[y] for x in res for y in op]
        self.ops = res
        
    def __iter__(self):
        self.idx = 0
        return self
    def next(self):
        if self.idx == len(self.ops):
            raise StopIteration
        res = tuple(self.ops[self.idx])
        self.idx = self.idx + 1
        return res

class Solution(object):
    def __init__(self):
        self.exprs = []
        self.idx = 0
    def __iter__(self):
        self.idx = 0
        return self
    def next(self):
        if self.idx == len(self.expr):
            raise StopIteration
        res = self.exprs[self.idx]
        self.idx = self.idx + 1
        return res
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        assert (num)
        if len(num) == 1:
            return None if eval(num) != target else num
        for ops in OpIterator('+-*', len(num)-1):
            expr = num[0]
            for i in xrange(len(num)-1):
                expr = expr + ops[i] + num[i+1]
            self.exprs.append(expr)
        res = []
        for expr in self.exprs:
            if eval(expr) == target:
                res.append(expr)
        return res

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

'''
for s in OpIterator('+-*', 2):
    print s

for s in product('+-*', repeat=2):
    print s

for s in getOp('+-*', 2):
    print s
'''


if __name__ == "__main__":
    s = Solution()
    res = s.addOperators('123', 6)
    assert (res == ['1+2+3', '1*2*3'])

    s = Solution()
    res = s.addOperators('232', 8)
    assert (set(res) == set(['2*3+2', '2+3*2']))

    s = Solution()
    res = s.addOperators('105', 5)
    assert (set(res) == set(['1*0+5' ]))

    s = Solution()
    res = s.addOperators('00', 0)
    assert (set(res) == set(["0+0", "0-0", "0*0"]))
