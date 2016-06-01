"""PANDIGITAL NUMBERS Problem-32
Each combination is tried and added if it works."""

from itertools import permutations,combinations

digits = range(1,10)
nb = 0
k = 0
computed = {}
for pandigit in permutations(digits,9):
    #print pandigit
    for divide in combinations(digits[:-1],2):
        n_str = ''.join([str(i) for i in pandigit])
        n1 = int(n_str[:divide[0]])
        n2 = int(n_str[divide[0]:divide[1]])
        n3 = int(n_str[divide[1]:])

        if n1*n2 == n3:
            computed[n3] = 1

print sum(computed)
