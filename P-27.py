"""QUADRATIC PRIMES Problem-27

fill_prime_list: given a full list of primes until one integer, this function fill the list
until another number.

Then for each a between the threshold and b (b>1 otherwise n = 0 does not work), the number of primes is
computed and the maximum is memorized.
In the end, this maximum is printed."""

def fill_prime_list(n,l):
    for i in range(l[-1]+1,n+1):
        is_prime = True
        for x in l[1:]: #The first element is 1, so it is relevant to remove it.
            is_prime = is_prime and (i % x != 0)
        if is_prime:
            l.append(i)

a_max = 1000
b_max = 1000

list_primes = [1]
m = 0
a_f = 0
b_f = 0
for a in range(-a_max+1,a_max):
    for b in range(1,b_max): #b has to be above 0 so that n = 0 can be a value.
        n = -1
        is_prime_sf = True
        while is_prime_sf:
            n += 1
            fill_prime_list(n**2 + a*n + b,list_primes)
            #print list_primes
            is_prime_sf = (n**2 + a*n + b in list_primes)

        if n > m:
            a_f = a
            b_f = b
            m = n

print a_f * b_f