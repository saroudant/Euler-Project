"""TRIANGULAR, PENTAGONAL AND HEXAGONAL Problem-45

To know whether a number is pentagonal or hexagonal, the second-order equation is solved
and if the result is an integer, then is said to be True.
n(3n-1)/2 = m => 3n^2 - n - 2*m = 0 so n = (1+sqrt(1+24m))/6 (because 24m > 1 for m > 0)
n(2n-1) = m => 2*n^2 - n - m = 0 so n = (1+sqrt(1+8m))/4

Every triangle number above 40755 are tried. If it is both hexagonal and pentagonal, then
the loop is broken and the result is returned."""

from math import *

def triangular(n):
    return n*(n+1)/2

def is_pentagonal(m):
    n = (1+sqrt(1+24*m))/6
    return int(n) == n

def is_hexagonal(m):
    n = (1+sqrt(1+8*m))/4
    return int(n) == n

n = 286
not_found = True

while not_found:
    m = triangular(n)
    if is_pentagonal(m) and is_hexagonal(m):
        not_found = False
        print m

    n += 1