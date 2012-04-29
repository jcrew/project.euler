#!/usr/bin/python
'''
Author: JAEYOON LEE (lee@jaeyoon.org)
Date: Sun Apr 29 14:39:31 PDT 2012
'''

def one(x):
    ''' Problem #1 (http://projecteuler.net/problem=1)
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000. '''
    res = 0
    for n in xrange(1, x):
        if n%3 is 0 or n%5 is 0:
            res += n
    return res

def test_one():
    assert(one(10)==23)
