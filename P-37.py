"""TRUNCATABLE PRIMES Problem-37

fill_prime_list : cf. problem 27, except 1 is removed
Truncating by the right is equivalent to a modulo
Truncating by the left is equivalent to a division (quotient)"""

from math import log

def fill_prime_list(n,l):
    for i in range(len(l)+1,n+1):
        is_prime = True
        for x in xrange(len(l)):
            if l[x] == 1:
                is_prime = (i % (x+1) != 0)
                if not is_prime:
                    break
        if is_prime:
            l.append(1)
        else:
            l.append(0)

nb = 11
nb_found = 0
n = 10
list_primes = [0,1]
list_truncatables = []

while nb_found <= nb:

    if str(n)[0] in ['0','1','2','4','6','8']:
        if str(n)[0] == '0':
            n += 3*int(10**int(log(n,10)))
        elif str(n)[0] == '1':
            n += 2*int(10**int(log(n,10)))
        else:
            n += int(10**int(log(n,10)))

    fill_prime_list(n,list_primes)
    is_truncatable = (list_primes[n-1] == 1)

    #checking if a multiple of 2 is in the list to remove a lot of cases:
    for i in xrange(10,2):
        if str(i) in str(n):
            is_truncatable = False
            break

    i = 1
    while is_truncatable and i < log(n,10)+2:
        is_truncatable = is_truncatable and (list_primes[max((n % 10**i) - 1,0)] == 1 or n % 10**i == 0)
        is_truncatable = is_truncatable and (list_primes[max((n // 10**i) - 1,0)] == 1 or n // 10**i == 0)
        i += 1

    if is_truncatable:
        nb_found += 1
        list_truncatables.append(n)
        print n
        print nb_found

    if n % 10000 == 0:
        print n

    n += 1

print sum(list_truncatables)