"""PERMUTED MULTIPLES Problem-52
same_digits compares two numbers to be sure that they have the same digits. To do so:
* If the two integers have different length, then it could not be possible.
* Else, the sets of digits are compared to be sure they are equal. In order to compare the
breakdown, the dictionary structure is used.
Then each number is tried until the one is found."""

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

nb_multiple = 6

n = 10
is_found = False

while not(is_found):
    n_same_digits = True
    for i in xrange(nb_multiple):
        n_same_digits = n_same_digits and same_digits(n,n*(i+1))
    n += 1
    is_found = n_same_digits

print n-1