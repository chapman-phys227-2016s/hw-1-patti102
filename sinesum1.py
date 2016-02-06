"""
File: sinesum1.py

Copyright (c) 2016 Taylor Patti

License: MIT

Sums sines and compares them to a step function.
"""    

from math import *

def S(t, n, T):
    sum = 0
    for i in range(n):
        sum = sum + ((2 * (i + 1) - 1)**-1) * sin((2 * (2 * (i + 1) - 1) * pi * t) / float(T))
    return sum*(4/pi)

def test_twosinesum():
    """checks that the S function is commensurate with direct calculation for t = 1, n = 2, T = 2pi"""
    apt = abs(S(1, 2, 2 * pi) - (4 / pi) * (sin(1) + sin(3) / 3)) < 1E-3
    msg = "Sums do not match."
    assert apt, msg
    
def f(t, T):
    if (t > 0) and (t < (T / float(2))):
        return 1
    elif t == T / float(2):
        return 0
    elif (t > (T / float(2))) and (t < T):
        return -1

def test_tequalTover2():
    apt = f(0.5, 1) == 0
    msg = "Equality wrong"
    assert apt, msg
    
def test_tgreaterTover2():
    apt = f(0.75, 1) == -1
    msg = "Greater than wrong."
    assert apt, msg
    
def difference(t, n, T):
    return f(t, T) - S(t, n, T)
    
def table(t):
    print
    print 'Difference Between the Limit and the Sum of Sines'
    print
    print '%10s %10s %10s %10s' % ('n', 'a=0.01', 'a=0.25', 'a=0.49')
    print
    n_list = [1, 3, 5, 10, 30, 100]
    alpha_list = [0.01, 0.25, 0.49]
    T = 2 * pi
    alpha1 = [difference(t*alpha_list[0], n_value, T) for n_value in n_list]
    alpha2 = [difference(t*alpha_list[1], n_value, T) for n_value in n_list]
    alpha3 = [difference(t*alpha_list[2], n_value, T) for n_value in n_list]
    for i in range(6):
        print '%10d %10.2f %10.2f %10.2f' % (n_list[i], alpha1[i], alpha2[i], alpha3[i])
        
table(1)


