"""PRIME PAIR SETS Problem-60

is_prime : True is n is prime
is_prime_set : concantenates both way and return True if both result integers
are prime.

Then, until a five set is found (5 can be changed by target), each prime is tested,
the list of all the primes that are making sets with it is added into sets and each
permutation is tested.
If one good is found, then the loop would be broken and the result return."""

from math import sqrt
from itertools import combinations

def is_prime(n):
    for k in range(2,int(sqrt(n))+1):
        if n%k == 0:
            return False
    return True


def is_prime_set(n,m):
    return is_prime(int(str(n)+str(m))) and is_prime(int(str(m)+str(n)))


target = 5

sets = {} #List of pairs indexed by the lowest element.
n = 2
not_found = True
combination = []

while not_found:
    if is_prime(n):
        sets[n] = []

        #Put all the numbers in sets that can be permuted
        for k in sets:
            if is_prime_set(k,n):
                sets[k].append(n)
                sets[n].append(k)

        #Test if one combination would work among the int that forms set with n
        for p in combinations(sets[n],target-1):
            is_comb = True

            #Test of each value of p if values are pairs.
            for i in p:
                for j in p:
                    is_comb = is_comb and (j in sets[i] or j == i)

            #If p is a combination, then the loop should break and the permutation returned. The last
            #value is is n
            if is_comb and len(sets[n]) >= target:
                combination = p
                not_found = False
                break

    n += 1

#n-1 since the last value has been added with 1
print sum(combination)+n-1