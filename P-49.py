"""PRIME PERMUTATIONS
same_digits : cf. pb-52 for more explanations
*First the list of the primes is drawn iteratively (for n the division by each
prime number under n is tried).
*Then only 4-digits primes are taken.
*The list of same-digits lists is drawn and tested to have the same difference (for 3-permutation)
*Finally, the known list is removed and the remaining one is concatenated. """

from itertools import permutations

def same_digits(k1,k2):
    if len(str(k1)) != len(str(k2)):
        return False
    else:
        k1_str = str(k1)
        k2_str = str(k2)

        k1_dico = dict()
        for l in k1_str:
            if l not in k1_dico:
                k1_dico[l] = 0
            k1_dico[l] += 1
        k2_dico = dict()
        for l in k2_str:
            if l not in k2_dico:
                k2_dico[l] = 0
            k2_dico[l] += 1

        return k2_dico == k1_dico

#List of primes until the threhsold.
prime_lists = [2]

for x in range(3,10000):
    is_prime = True
    for e in prime_lists:
        is_prime = is_prime and (x % e != 0)
    if is_prime:
        prime_lists.append(x)

prime_lists = [x for x in prime_lists if x >= 1000]

#List of same-digits primes couples ordered.
same_digits_prime = [(x,y) for x in prime_lists for y in prime_lists if same_digits(x,y) and x <= y]

prime_same_digits_breakdown = dict()
for e in same_digits_prime:
    if e[0] not in prime_same_digits_breakdown:
        prime_same_digits_breakdown[e[0]] = []
    prime_same_digits_breakdown[e[0]].append(e[1])

#Couples are gathered into bigger lists.
prime_same_digits_breakdown = [prime_same_digits_breakdown[e] for e in prime_same_digits_breakdown if len(prime_same_digits_breakdown[e]) >= 3]

#Breakdown of those lists in 3-permuted listed. For each permutation difference with one another is tested.
prime_same_digits_breakdown_with_diff = []
for tp in prime_same_digits_breakdown:
    perm = permutations([i for i in xrange(len(tp))],3)
    for p in perm:
        if (tp[p[1]] - tp[p[0]] == tp[p[2]] - tp[p[1]]) and (tp[p[0]] < tp[p[1]]) and (tp[p[1]] < tp[p[2]]):
            prime_same_digits_breakdown_with_diff.append([tp[p[0]],tp[p[1]],tp[p[2]]])

only_4digit_else = [[str(x) for x in e] for e in prime_same_digits_breakdown_with_diff if 1487 not in e]

print ''.join(only_4digit_else[0])