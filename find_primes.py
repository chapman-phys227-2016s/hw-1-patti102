#! /usr/bin/env python

"""
File: find_primes.py

Copyright (c) 2016 Taylor Patti

License: MIT

Finds primes by elimination of multiples of smaller values in and below a given
value n, then returns a list of the prime numbers.
"""    

def find_primes(n):
    """finds all of the prime numbers of n and below by eliminating mutiples
    of smaller numbers from a master list"""
    num_list = range(n + 1)
    num_list = num_list[2:]
    for i in num_list:
        p = i + i
        while p <= max(num_list):
            if p in num_list:
                num_list.remove(p)
            p = p + i
    return num_list

def test_firstfourprimes():
    """ensures that the list produced is equal to [2, 3, 5, 7], the
    prime numbers corresponding to the value n=10"""
    apt = find_primes(10) == [2, 3, 5, 7]
    msg = "These are not the primes you're looking for."
    assert apt, msg