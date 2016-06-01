"""DISTINCT POWERS Problem-29
a**b is decomposed using the log.
Since the log computation is chaotic, it is truncated.
The truncated coefficient differs and the value that occurs the most is taken
(big enough for being relevant, but small enough to remove problems)"""
from math import log,floor

a_min = 2
a_max = 100
b_min = 2
b_max = 100

list_found = []
for i in range(1,20):
    list_power = []
    for a in range(a_min,a_max+1):
        for b in xrange(b_min,b_max+1):
            if floor((10**i)*b*log(a)) not in list_power:
                list_power.append(floor((10**i)*b*log(a)))
    list_found.append(len(list_power))

elements = dict()

for elt in list_found:
    if elt in elements:
        elements[elt] += 1
    else:
        elements[elt] = 1

print elements