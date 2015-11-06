'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        '''
        1. If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
        2. If the total number of gas is bigger than the total number of cost. There must be a solution.
'''
        gasLeft = 0
        start = 0
        for (g, c) in zip(gas, cost):
            gasLeft += g - c
            if gasLeft < 0:
                gasLeft = 0
                start += 1
        return start if gasLeft >= 0 else -1

def generateGasAndCost():
    gas =  [1, 2, 2, 1, 2, 2]
    cost = [2, 3, 1, 1, 1, 2]
    assert (sum(gas) >= sum(cost))
    return (gas, cost)
                
if __name__ == '__main__':
    (gas, cost) = generateGasAndCost()
    print Solution().canCompleteCircuit(gas, cost)

        
