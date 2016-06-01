"""DIGIT FIFTH POWER Problem-30
The method used here is quite brutal:
* First a majorant is found using the monotonie of the underlying function
* Then for the values in between, a test is done that add relevant value
* Finally those values are added."""

from math import *

pow = 5
#First we found a maximum value since
#n <= (log(n)+1) * 9 ** pow (n <= 99..99)

mx = 1
prod = 9 ** pow
while mx <= (log(mx)+1) * prod:
    mx += 1


#list of the i**5
list_powers = [i**pow for i in xrange(10)]
list_numbers = []

#For each value the summation is tried using the last list so that those value have not to be recomputed.
for i in xrange(10,mx):
    if sum([list_powers[int(e)] for e in str(i)]) == i:
        list_numbers.append(i)

print sum(list_numbers)
