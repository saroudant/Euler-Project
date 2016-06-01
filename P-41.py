"""PANDIGITAL PRIME Problem-41

A 9-digit pandigital number cannot be prime since 1+2+..+9 = 45 = 3*15
The same for 8 since 36 = 12*3
So the maximum number would be a 7-pandigital number.

is_prime: try the division by every number until sqrt(n). If one divide n, then n is not prime.
Then starting from 7 every permutation of (1,2,..n) is tested. If one permutation works, then
the loop is stopped and the maximum is taken."""

from math import sqrt
from itertools import combinations,permutations

def is_prime(n):
    """
    :param n: number you want to test
    :param l: list of primes below n
    """
    for e in range(2,int(sqrt(n))+1):
        if n % e == 0:
            return False
    return True

mx = 3

n = 7
not_found = True
primes = []
while not_found and n >= 0:
    for c in combinations(range(1,n+1),n):
        for p in permutations(c):
            str_int = ''
            for i in xrange(len(p)):
                str_int += str(p[i])
            if is_prime(int(str_int)):
                primes.append(int(str_int))
                not_found = False
    n -= 1

print max(primes)


