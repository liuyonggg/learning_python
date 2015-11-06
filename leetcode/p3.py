'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        assert (len(tokens))
        operands = []
        for i in xrange(len(tokens)):
            if (self.isOperation(tokens[i])):
                assert (len(operands))
                op2 = operands.pop()
                op1 = operands.pop()
                r = self.eval(tokens[i], [op1, op2])
                operands.append(r)
            else:
                operands.append(int(tokens[i]))
        assert len(operands)
        return operands[0]
    def isOperation(self, s):
        return s == '+' or s == '-' or s == '*' or s == '/'
    def eval(self, operation, oprands):
        r = None
        if operation == '+':
            r = self.add(oprands)
        elif operation == '-':
            r = self.sub(oprands)
        elif operation == '*':
            r = self.mul(oprands)
        else:
            assert (operation == '/')
            r = self.div(oprands)
        return r

    def add(self, oprands):
        r = 0
        for i in xrange(len(oprands)):
            r += oprands[i]
        return r
    def sub(self, oprands):
        r = oprands[0]
        for i in xrange(1, len(oprands)):
            r -= oprands[i]
        return r
    def mul(self, oprands):
        r = 1
        for i in xrange(len(oprands)):
            r *= oprands[i]
        return r
    def div(self, oprands):
        r = oprands[0]
        for i in xrange(1, len(oprands)):
            r /= oprands[i]
        return r



if __name__ == "__main__":
    assert (Solution().evalRPN(["2", "1", "+", "3", "*"]) ==  9)
    assert (Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6)
