'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [eval(`a`+c+`b`)
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
    def diffWaysToCompute2(self, input):
        return [
            eval('a' + c + 'b')
            for i, c in enumerate(input) if c in "+-*"
            for a in self.diffWaysToCompute2(input[:i])
            for b in self.diffWaysToCompute2(input[i+1:])
            ] or [int(input)]

if __name__ == "__main__":
    print Solution().diffWaysToCompute("2-1-1")
    print Solution().diffWaysToCompute("2")
