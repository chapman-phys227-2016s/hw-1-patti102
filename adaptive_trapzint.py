"""
File: adaptive_trapzint.py

Copyright (c) 2016 Taylor Patti

License: MIT

This code establishes and compares functions of various complexities which use trapezoids to estimate the area under curves in the plane.
""" 

import math
#from sympy import symbols, integrate, lambdify

def trapzint(f, a, b, n):
    """Estimates integral by the construction of n evenly spaced trapezoids on the interval [a, b]"""
    h = (b-a)/float(n)
    sum = 0
    for i in range(n):
        #h serves double duty as both the x-distance width and the x-distance increment
        sum = sum + (1.0/2)*h*(f(a + h*i)+f(a + h*(i+1)))
    return sum

def square(t):
    return 2

def test_square():
    """A two by two square is measured and should have area 4."""
    apt = (abs(trapzint(square, 0, 2, 20)-4) < 1E-6)
    msg = "Not square area."
    assert apt, msg

def test_sinusoidal():
    """Ensures that the area of sin from 0 to pi/2 is 1."""
    apt = (abs(trapzint(math.sin, 0, math.pi/2, 1000)-1)<1E-6)
    msg = "Not sin area."
    assert apt, msg

def second_derivative(f, x, h=1e-6):
    return (f(x-h) - 2*f(x) + f(x+h))/float(h**2)

def max_second_derivative(f, a, b, n=1000000):
    """Obtains the maximum absolute value of the second derivative of a function at n points."""
    inc = (b-a)/float(n)
    max = abs(second_derivative(f, a))
    for i in range(n):
        candidate = abs(second_derivative(f, a + inc*(i+1)))
        if candidate > max:
            max = candidate
    return max

def test_sin_maxderivative():
    """sin's max derivative should be 1"""
    apt = (abs(max_second_derivative(math.sin, 0, 2*math.pi) - 1) < 1E-3)
    msg = "Wrong derivative for sin"
    assert apt, msg
    

def adaptive_trapzint(f, a, b, eps=1E-5):
    """Calculates the number of intervals required to obtain integral estimation within some precision and implements trapzint with this value."""
    h = math.sqrt(12*eps)*(((b-a)*max_second_derivative(f, a, b))**(-1/2.0))
    n = (b-a)/float(h)
    #ceil taken to ensure the integrity of the inequality
    n = int(math.ceil(n))
    return trapzint(f, a, b, n), n

def curve(x):
    return x**2 + x + 1

def test_adaptive_limits():
    """ensures that the n value given is sufficient for the curve function.
    This function has calculated n of 366 on the interval 0 to 2"""
    t = symbols('t')
    curve_func = t**2 + t + 1
    integ = integrate(curve_func, t)
    value = lambdify([t], integ)
    value = value(2)
    print value
    apt = abs(adaptive_trapzint(curve, 0, 2)[0]-value)<1E-5
    msg = "N is too small."
    assert apt, msg

def preformance_table(function_tuples=[('cos(x)', math.cos, [0.0, math.pi]), ('sin(x)', math.sin, [0.0, math.pi]), ('sin(x)', math.sin, [0, math.pi/2.0])]):
    """Outputs the function, interval, error, and n values into a table. Note that here, the exact answers were simply given in an
    array as these integrals were considered both common and fundamental knowledge. If you would like to see an example of symbolic integration and subsequent
    numerical evaluation, please see above the function 'test_adaptive_limits'"""
    exact = [0, 2, 1]
    print
    print 'Preformance Table of Various Functions'
    print
    print '%10s %15s %15s %15s' % ('Function', 'Interval', 'Error', 'N-value')
    print
    for i in function_tuples:
        value, nvalue = adaptive_trapzint(i[1], i[2][0], i[2][1])
        error = value-exact[function_tuples.index(i)]
        print '%9s %10.2f %2s %3.2f %17E %9d' % (i[0], i[2][0], 'to', i[2][1], error, nvalue)
        print

preformance_table()
