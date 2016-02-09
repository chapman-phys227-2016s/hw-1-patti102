#! /usr/bin/env python

"""
File: centered_diff.py

Copyright (c) 2016 Taylor Patti

License: MIT

Takes the first derivative of functions numerically and demonstrates this with a set of
functions and a resulting table.
"""    

from math import *
from sympy import diff, lambdify, symbols

def numdiff(f, x, h=1E-5):
    """takes the first derivative of function f"""
    return (f(x + h) - f(x - h)) / (2 * float(h))

def quadratic(x):
    return x**2 + x + 1

def test_quaddiff():
    apt = (abs(numdiff(quadratic, 2) - 5) < 1E-10)
    msg = "Derivatives do not match."
    assert apt, msg

def application():
    """makes list of the difference between the estimated derivative for h=0.01 and
    the analytical derivative"""
    application_list = []
    x = symbols('x')
    print
    print '%20s %20s' % ('Function', 'Error')
    print
    funcvar_tuples = [(lambda t: exp(t), 'exp(x)', float(0)), (lambda t : exp(-2*t**2), \
    'exp(-2*x**2)', float(0)), (lambda t: cos(t), 'cos(x)', 2*pi), (lambda t: log(t), \
    'log(x)', float(1))]
    for i in funcvar_tuples:
        prime = diff(i[1], x)
        exact = lambdify([x], prime)
        error = numdiff(i[0], i[2], 0.01) - exact(i[2])
        print '%20s %21.2E' % (i[1], error)
        print
        application_list.append(error)
    return application_list

def test_accuracycheck():
    """ensures that each item in application is bellow a certain threshold
    and thus above a certain accuracy"""
    f = application()
    apt = True
    for i in f:
        if abs(i) > 1E-3:
            apt = False
    msg = "Too large of an error."
    assert apt, msg
