"""TOTIENT MAXIMUM Problem-69

In this question the Euler function is decomposed to make it easy to compute.
First the primes until sqrt(n_max) are calculated. Then the phi is calculated by
computing the inverse of the primes that divide n."""

from math import sqrt

def product(a,b):
    return a*b


def phi(n,primes):
    """
    Computation using the formula : n * prod(1-1/p) for p prime that divides n
    """
    prime_decomp = [1. - 1./j for j in primes if n >= j and n % j == 0]
    return n * reduce(product,prime_decomp,1)

n_max = 1000000

#List of primes for dividing all the numbers
primes = []
for i in range(2,int(sqrt(n_max))):
    is_prime = True
    for k in primes:
        if i % k == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)

values = [1.*j/phi(j,primes) for j in range(2,n_max+1)]
print values.index(max(values))+2