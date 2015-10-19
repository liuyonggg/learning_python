'''
this is exercise 2
from it, you should learn how to manipulate string, also know how to do calculation
the exercise should be finisehd before 11/22
'''

import unittest

def find_all(s, c):
    '''
    return all indexes of c in s, if c is not in s return none
    for example: find_all("hello", 'l') will return [2, 3]
    :type s: string
    :type c: string
    :rtype : list of index
    '''
    pass

def has_all(s, l):
    '''
    return if s has all strings in l
    for example: 
        has_all("hello", ['l', 'o']) will return True
        has_all("hello", ['l', 'o', 'a']) will return False
    :type s: string
    :type l: list of string
    :rtype : bool True if has all, otherwise False
    '''
    pass

def reverse_list(l):
    '''
    return reversed l
    for example: 
        reverse_list([1, 2, 3]) will return [3, 2, 1]
    :type l: list
    :rtype : list
    '''
    pass

def calculate_present_value(future_value, interest, number_of_periods):
    '''
    return present value
    please refer definition of present definition at https://en.wikipedia.org/wiki/Present_value
    present value = future_value/(1+interest)^^number_of_period
    :type future_value: float: future value
    :type interest: float: annual interest
    :type number_of_periods: integer: number of periods(year)
    :rtype: float: present value
    '''
    pass

def calculate_life_time_present_value(cache_flow, interest, number_of_periods):
    '''
    return present value of life time annual income
    please refer definition of present definition at https://en.wikipedia.org/wiki/Present_value
    present value = cache_flow/(1-(1+interest)^^(-number_of_periods))/interest
    :type cache_flow: float: annual cache flow
    :type interest: float: annual interest
    :type number_of_periods: integer: number of periods(year)
    :rtype: float: present value
    '''
    pass


'''
below are for teacher, student shouldn't make change
'''

class testexe2(unittest.TestCase):
    def test_find_all(self):
        assert find_all("hello", 'l') == [2, 3]
        assert find_all("I am conner, conner I am.", 'conner') == [5, 13]

    def test_has_all(self):
        assert has_all("hello", ['l','o'])
        assert has_all("hello", ['l','o', 'a'])
    
    def test_reverse_list(self):
        assert reverse_list([1, 2, 3]) == [3, 2, 1]
        assert reverse_list([1, 1, 2, 3]) == [3, 2, 1, 1]

    def test_calculate_present_value(self):
        assert self.assertAlmostEqual(calculate_present_value(121, 0.1, 2), 100.0)

    def test_calculate_life_time_present_value(self):
        assert self.assertAlmostEqual(calculate_present_value(200000, 0.03, 40), 9613861.75344)
        

if __name__ == '__main__':
    unittest.main()
