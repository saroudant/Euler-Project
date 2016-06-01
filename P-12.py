"""HIGHLY DIVISIBLE TRIANGULAR NUMBERS Problem-12
* First the function divisors take a look at all the numbers between n and sqrt(n)
and add 2 to the number (i and n/i divide n). 1 is remove if n is a perfect square : in
this case only 1 is added instead of 2 previously.
* Then the different cases are crossed iteratively and stop when the target is reached."""

from math import sqrt,floor

def divisors(n):
    nb = 0
    for j in range(1,int(sqrt(n))+1):
        if n % j == 0:
            nb += 2
    if floor(sqrt(n)) == sqrt(n):
        nb -= 1
    return nb

target = 500
n = 1
s = 1
nb_max = divisors(s)

while nb_max < target:
    n += 1
    s += n
    nb_max = max(divisors(s),nb_max)

print s