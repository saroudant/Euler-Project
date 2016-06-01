__author__ = 'mourragui'
from copy import copy
from random import random
from numpy import *

""" SCORING PROBABILITIES Problem 286
Thanks to a Bayesian decomposition the probability computation is broken down into two
smaller problems. The problem is just to compute recursively those values.
The number of computations is exponential, thus the different values are stored into a
matrix named matrix.

The probability is now computed, a dichotomie is then operated to find the right value."""

def compute_density(q,mx,mn,y):
    matrix = zeros((mx-mn+2,y+1))
    mxg = mx
    qg = q

    def rec_density(a,b):

        if b < 0:
            return 0
        elif mxg == a and b == 1:
            #print 'hello'
            #print 1 - mxg / qg
            return 1 - mxg / qg
        elif mxg == a and b == 0:
            #print 'hello'
            return mxg / qg
        elif mxg == a and b > 1:
            return 0
        else:
            if matrix[a+1][b-1] == 0.:
                matrix[a+1][b-1] = rec_density(a+1,b-1)
            if matrix[a+1][b] == 0.:
                matrix[a+1][b] = rec_density(a+1,b)

            return ((qg - a)*matrix[a+1][b-1] + a * matrix[a+1][b]) / qg

    return rec_density(mn,20)


#print compute_density(52.,50.,1.,20.)
cible = 0.02
mn = 52
mx = 53
eps = 0.00000000001

x = compute_density((mx+mn)/2,50.,1.,20.)

while mx - mn > eps:
    if x > cible :
        mn = (mn+mx) / 2.
        print "c'est plus"
    else:
        mx = (mn+mx) / 2.

    x = compute_density((mx+mn)/2.,50.,1.,20.)

print (mx+mn)/2