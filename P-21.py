"""AMICABLE NUMBERS Problem 21
divisors : give the list of all the divisors
d : give the sum of all the divisors

liste_d : liste of d(n) for n between 1 and 10000
liste_amicable : liste of all amicables. liste_d is iterated and
amicable values are taken away fom it.
Finally liste_amicable is sumed."""

def divisors(n):
    div = []
    for i in range(1,n):
        if n % i == 0:
            div.append(i)
    return div

def d(n):
    return sum(divisors(n))

mx = 10000
liste_d = [0]
for i in range(1,mx):
    liste_d.append(d(i))

liste_amicable = []
for i in range(1,mx):
    if liste_d[i] < mx and liste_d[liste_d[i]] == i and i != liste_d[i]:
        liste_amicable.append(i)

print sum(liste_amicable)