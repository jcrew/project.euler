#!/usr/bin/python
'''
Author: JAEYOON LEE (lee@jaeyoon.org)
Date: Sun Apr 29 14:39:31 PDT 2012
Test: python -m unittest eula
'''

import unittest

class EULA():
    def __init__(self):
        self.answer = {}

    def one(self, x):
        ''' Problem #1 (http://projecteuler.net/problem=1)
        If we list all the natural numbers below 10 that are multiples of 3 or 5,
        we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000. '''
        self.answer['one'] = 0
        for n in xrange(1, x):
            if n % 3 is 0 or n % 5 is 0:
                self.answer['one'] += n
        return self.answer['one']


    def two(self, x):
        ''' Problem #2 (http://projecteuler.net/problem=2)
        Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
        By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
        find the sum of the even-valued terms. '''
        self.answer['two'] = 0
        a, b = 0, 1
        while b < x:
            if b % 2 is 0:
                self.answer['two'] += b
            a, b = b, a+b

        return self.answer['two']


class test_EULA(unittest.TestCase):
    def setUp(self):
        self.eula = EULA()

    def test_one(self):
        self.assertEqual(self.eula.one(10), 23)

    def test_two(self):
        self.assertEqual(self.eula.two(80), 44)

    if __name__ == '__main__':
        unittest.main()
