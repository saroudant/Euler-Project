"""PRIME SUMMATIONS Problem-77

In problem-76 it was saw that 100 can be written in ,more than 10^8 possible ways. Therefore
taking the first prime until 100 makes sense.

The same algorithm as P-76 is used but this time only using primes in the summation. The only thing that needed
to be added was a condition : for each iteration, adding one to the nbre_perm since the iteration is
made on primes."""

from math import sqrt

target = 5000
assump_max = 100

primes = [k for k in range(2,100) if 0 not in [k%j for j in range(2,int(sqrt(k))+1)]]
nbre_perm = [0]*(assump_max+1)

for i in primes:
    nbre_perm[i] += 1

    for k in range(i,assump_max+1):
        nbre_perm[k] += nbre_perm[k-i]

values_above_target = [i for i in xrange(assump_max+1) if nbre_perm[i] > target]
print values_above_target[0]